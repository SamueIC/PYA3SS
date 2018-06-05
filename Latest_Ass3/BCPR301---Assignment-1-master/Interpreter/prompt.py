from cmd import Cmd
from Interpreter.controller import Controller
from os import path, chdir, getcwd
import re
# from re import match, search


class Shell(Cmd):
    # This will replace the init stuff, all of it will be set in the parent class, access
    # these values using self.intro, self.prompt etc

    # if the init is defined then super must be used and each item attached to the object, may be better approach
    # because it is more explicit
    def __init__(self):
        super().__init__()
        self.controller = Controller()
        self.intro = "Welcome to our custom Interpreter shell. Type help or ? to list commands.\n"
        self.prompt = '(Interpreter) '
        self.file = None
        self.directory = path.realpath(path.curdir)

    # Wesley
    def do_cd(self, arg):
        """
        Syntax:
            cd [path]
            relative traversal through file structure, same as windows

        :param arg:
            path: [string]

        :return:
            New working directory
        """
        try:
            line = arg.lower()
            start_path = path.realpath(path.relpath(line))
            if self.directory is None and path.isdir(start_path):
                self.directory = start_path
                print(self.directory)
            elif path.isdir(path.realpath(path.relpath(path.join(self.directory, line)))):
                self.directory = path.realpath(path.relpath(path.join(self.directory, line)))
                print(self.directory)
            else:
                print("Not a valid directory")
        except ValueError:
            print("No path was specified, please try again")
        except TypeError:
            print("Type of none is invalid")
        finally:
            print("You are now working in..")
            print(self.directory)

    def do_load(self, arg):
        """
        Syntax:
            load [filename] or [database]

        :param arg:
            filename: [string]

        :return:
            File has been set
        """
        if arg.lower() != "-database":
            try:
                if path.isfile(path.realpath(path.join(self.directory, path.relpath(arg)))):
                    self.file = path.realpath(path.join(self.directory, path.relpath(arg)))
                    result = self.controller.load(self.file)
                    if result:
                        self.prompt = '(Interpreter: ' + path.basename(self.file) + ') '
                        self.controller.validate()
                    else:
                        self.prompt = '(Interpreter)'
                else:
                    print("File not found")
            except ValueError:
                print("No path was specified, please try again")
            except Exception as e:
                print("this errror comes from do_load in prompt")
                print(e)

        elif arg.lower() == "-database":
            db = input("remote or local?")
            try:
                if db.lower() == "local":
                    db_name = input("What is the name of the database? >")
                    self.controller.set_local(db_name)
                    self.controller.get_local()
                    try:
                        self.controller.check_data()
                        print("Data has been loaded")
                    except ValueError as ve:
                        print("No graph_data was found")
                        print(ve)
                    except Exception as e:
                        print(e)

                elif db.lower() == "remote":
                    host = input("What is the hostname? >")
                    user = input("What is the username? >")
                    password = input("Input a password >")
                    db = input("What is the database name? >")
                    self.controller.set_remote(host, user, password, db)
                    self.controller.get_remote()
                    try:
                        self.controller.check_data()
                        print("Data has been loaded")
                    except ValueError as ve:
                        print("No graph_data was found")
                        print(ve)
                    except Exception as e:
                        print(e)
                else:
                    print("invalid database type")
            except ValueError:
                print("Try again...")
            except AttributeError:
                print("No graph_data found")
            except Exception as e:
                print(e)
        else:
            print("Invalid command")

    def do_graph(self, arg):
        """
        Syntax:
            graph [graphtype] [filename]
            Displays a graph of the loaded graph_data

        :param arg:
            graphtype: [-bar | -scatter | -pie]
            filename: [string]

        :return:
            The graph
        """
        commands = arg.split(" ")
        # James exception handling
        if self.controller.check_data():
            try:
                if commands[0] == "pie" or commands[0] == "scatter" or commands[0] == "bar":
                    a_path = path.join(self.directory, commands[1] + ".html")
                    self.controller.set_graph(commands[0], a_path)
                    criteria = input("What are the criteria? ([key] [value - optional]) > ")
                    crit = criteria.split(" ")
                    if len(crit) > 1:
                        # Feature Envy refactoring controller.graph.set_criteria
                        self.controller.set_criteria(crit[0], crit[1])
                    else:
                        # Feature Envy refactoring
                        self.controller.set_criteria(crit[0])
                    keys = input("What keys to use? ([key1] [key2]) > ")
                    a_key = keys.split(" ")
                    if len(a_key) > 1:
                        self.controller.set_keys(a_key[0], a_key[1])
                    else:
                        self.controller.set_keys(a_key[0])
                    title = input("What is the title? >")
                    if len(a_key) > 1:
                        self.controller.draw(a_key[0], a_key[1], title)
                    else:
                        self.controller.draw(a_key[0], a_key[0], title)

                else:
                    print("filename is invalid")
            except IndexError:
                print("You have entered invalid criteria")
            except KeyError:
                print("This key is invalid")
        else:
            print("Please set graph_data before attempting to create a graph")

    def do_quit(self, arg):
        """
        Syntax:
            quit
            Quit from my CMD

        :param arg:
            none

        :return:
            True
        """
        print("Quitting ......")
        return True

    def do_pwd(self, arg):
        """
        Syntax:
            pwd
            Print the current working directory

        :param arg:
            none

        :return:
            The current working directory
        """
        print(self.directory)

    def do_save(self, arg):
        """
        The save function works by saving the loaded file's graph_data to the specified database name and type.
        Syntax: save [database type]
        :param arg: Local = Locally saved database. Saves in the working current working directory.
                    Remote = Remotely stored database. Not saved to local machine.
        :return:
        """
        commands = arg.split(" ")
        if self.controller.check_data():
            try:
                if commands[0].lower() == "local":
                    db_name = input("What would you like to name the database? >")
                    self.controller.set_local(db_name)
                elif commands[0].lower() == "remote":
                    host = input("What is the hostname? >")
                    user = input("What is the username? >")
                    password = input("Input a password >")
                    db = input("What is the database name? >")
                    self.controller.set_remote(host, user, password, db)
                else:
                    print("invalid database type")
            except ValueError:
                print("Try again...")
        else:
            print("Please load graph_data before attempting to save")


if __name__ == '__main__':
    Shell().cmdloop()
