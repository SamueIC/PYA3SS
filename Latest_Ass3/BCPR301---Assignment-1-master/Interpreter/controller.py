from database_handler import DatabaseHandler
from filehandler import FileTypeAbstract, FileTypeCSV, FileTypeTXT, FileTypeXLSX
from validator import Validator
from os import path
from chart import Graph, GraphType, PieGraph, BarGraph, ScatterGraph, ConcreteBar, ConcretePie, ConcreteScatter
from pathlib import Path, PurePosixPath
from filehandler import FileTypeTXT, FileTypeXLSX, FileTypeCSV


# Wesley
class Controller:
    def __init__(self):
        self.db_handler = DatabaseHandler()
        self.data = None
        self.filehandler = None
        self.graph = None

    def load(self, filename):
        """
        Set the file that will create the filehandler object
        """
        if path.exists(filename):
            self.filehandler = self.return_reader(filename)
            self.filehandler.filename = filename
            return True
        else:
            return False

    # noinspection PyMethodMayBeStatic
    def return_reader(self, filename):
        suffix = PurePosixPath(filename).suffix
        if suffix == '.csv':
            return FileTypeCSV()
        elif suffix == '.xlsx':
            return FileTypeXLSX()
        elif suffix == '.txt':
            return FileTypeTXT()
        else:
            print("File extension unknown")

    def validate(self):
        """
        Read selected file
        """
        result = self.filehandler.template_method()
        self.data = result
        print("")
        print(result)

    def set_local(self, connection):
        """
        Set the local database with a specified name
        :param connection:
        :return:
        """
        self.db_handler.set_local(connection)
        self.db_handler.insert_local_dict(self.data)

    def set_remote(self, host, user, password, db):
        """
        Set the remote database
        :param host, user, password, db:
        :return:
        """
        self.db_handler.set_remote(host, user, password, db)
        self.db_handler.insert_remote_dict(self.data)

    def set_graph(self, graph_type, filename):
        types = {
            'pie': ConcretePie(),
            'scatter': ConcreteScatter(),
            'bar': ConcreteBar()
        }
        self.graph = types[graph_type]
        self.graph.set_file_name(filename)
        self.graph.set_graph_type(self.data)

    def get_local(self):
        self.data = self.db_handler.get_local()

    def get_remote(self):
        self.data = self.db_handler.get_remote()

    def set_criteria(self, criteria_1, criteria_2=None):
        self.graph.set_criteria(criteria_1, criteria_2)

    def set_keys(self, key_1, key_2=None):
        self.graph.set_keys(key_1, key_2)

    def draw(self, x, y, title):
        self.graph.draw(x, y, title)

    def check_data(self):
        if self.data is not None:
            return True
        return False
