from Interpreter.database_local import DBLocal
from Interpreter.database_remote import DBRemote
from Interpreter.pickler import Pickler
# from unpickler import Unpickler


# Wesley
class DatabaseHandler:
    def __init__(self):
        self.local = DBLocal()
        self.remote = DBRemote()
        self.local_connection = None
        self.remote_connection = None

    # A really, really, really bad decorator that can get fixed in ass2 //Wesley
    def local_decorator(f):
        def wrapper(*args):
            db = args[0].local_connection
            args[0].local.connect(db)
            # if args[0].local_connection == ":memory:":
            args[0].local.create_table()
            r = f(*args)
            args[0].local.commit()
            args[0].local.close()
            return r
        return wrapper

    # Part 2 of really, really, badness //Wesley
    def remote_decorator(f):
        def wrapper(*args):
            db = args[0].remote_connection
            args[0].remote.connect(db["host"], db["user"], db["password"], db["db"])
            args[0].remote.create_table()
            r = f(*args)
            args[0].remote.commit()
            args[0].remote.close()
            return r
        return wrapper

    # Wesley
    def set_local(self, connection=":memory:"):
        self.local_connection = connection

    # Wesley
    def set_remote(self, host, user, password, db):
        self.remote_connection = {"host": host, "user": user, "password": password, "db": db}

    # Wesley
    @local_decorator
    def insert_local_dict(self, dictionary):
        """Insert values into both the local and remote"""
        pickled = Pickler.pickle_unpickle(dictionary)
        self.local.insert_dictionary(pickled)
        # print(self.local.get_db())

    # Wesley
    @remote_decorator
    def insert_remote_dict(self, dictionary):
        """Insert values into both the local and remote"""
        pickled = Pickler.pickle_unpickle(dictionary)
        self.remote.insert_dictionary(pickled)
        # print(self.remote.get_db())

    # Wesley
    @local_decorator
    def get_local(self):
        unpickle = Pickler.pickle_unpickle(self.local.get_db())
        return unpickle
        # print(unpickle)

    # Wesley
    @remote_decorator
    def get_remote(self):
        unpickle = Pickler.pickle_unpickle(self.remote.get_db())
        return unpickle
        # print(unpickle)

    # Wesley
    @local_decorator
    def drop_local_table(self):
        self.local.drop_table()

    # Wesley
    @remote_decorator
    def drop_remote_table(self):
        self.remote.drop_table()

