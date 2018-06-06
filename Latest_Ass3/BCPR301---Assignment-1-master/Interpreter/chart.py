from plotly import offline
from plotly.graph_objs import Scatter, Layout, Pie, Bar
from abc import ABCMeta, abstractmethod
import doctest


class GraphType(metaclass=ABCMeta):
    def __init__(self):
        self.filename = None
        self.graph_data = None

    @abstractmethod
    def draw_graph(self, x_key, y_key, title):
        pass

    def set_this_criteria(self, key, statistic=None):
        """
        This will search through the given dictionary and return each employee
        that matches the criteria
        e.g. return a dictionary with all people where their gender is male
        :param dictionary: the graph_data that will be used
        :param key: the key value in the dictionary you would like to search
        :param statistic: the set value you would like to search
        :return:
        >>> g = Graph()
        >>> g.graph_type.graph_data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}, 1: {"IhD": "A2f3", "Gender": "Female", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}}
        >>> g.graph_type.set_criteria("Gender", "Male")
        {0: {'1ID': 'A23', 'Gender': 'Male', 'Age': 22, 'Sales': 245, 'BMI': 'normal', 'salary': 20, 'Birthday': '24/06/1995'}}
        """
        if statistic is not None:
            self.graph_data = {record[0]: record[1] for record in self.graph_data.items() if record[1][key] == statistic}
        return self.graph_data

    def set_data_keys(self, labels, data):
        """
        :param dictionary:
        :param key_a:
        :param key_b:
        :return:
        >>> g = Graph()
        >>> g.set_data({"dfd":"asdfds"}, "bar", "C:\\temp\\random.html")
        >>> g.graph_type.graph_data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}, 1: {"IhD": "A2f3", "Gender": "Female", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}}
        >>> g.graph_type.set_data_keys("Gender", "Sales")
        {'Gender': ['Male', 'Female'], 'Sales': [245, 245]}
        """
        keys_a = list()
        keys_b = list()
        for (key, value) in self.graph_data.items():
            for (key1, value1) in value.items():
                if key1 == labels:
                    keys_a.append(value1)
                if key1 == data:
                    keys_b.append(value1)
        self.graph_data = {labels: keys_a, data: keys_b}
        return self.graph_data

    def set_graph_data(self, data):
        self.graph_data = data

    def set_file_name(self, filename):
        self.filename = filename


class ScatterGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Scatter(x=self.graph_data[x_key], y=self.graph_data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


class PieGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        """

        :param x_key:
        :param y_key:
        :param graph_title:
        :return:
        """
        print("self.graph_data ===========================")
        print(self.graph_data)
        offline.plot({
            "data": [Pie(labels=self.graph_data[x_key], values=self.graph_data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


class BarGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Bar(x=self.graph_data[x_key], y=self.graph_data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Creator ABC
class Graph(metaclass=ABCMeta):
    def __init__(self):
        self.graph_type = self.factory_method()

    @abstractmethod
    def factory_method(self):
        pass

    def set_file_name(self, filename):
        self.graph_type.set_file_name(filename)

    def set_graph_type(self, data):
        """
        Set the graph_data to be used
        :param dictionary: Will contain the graph_data that will be used
        :param a_type: set the type of graph to generate
        :param filename: sets the save location and file name
        :return: void
        """
        self.graph_type.set_graph_data(data)

    def set_criteria(self, criteria_1, criteria_2):
        print("self.graph_type ==========================================")
        print(self.graph_type)
        self.graph_type.set_this_criteria(criteria_1, criteria_2)

    def set_keys(self, key_1, key_2):
        self.graph_type.set_data_keys(key_1, key_2)

    def draw(self, x_key, y_key, title):
        self.graph_type.draw_graph(x_key, y_key, title)


class ConcreteBar(Graph):
    def factory_method(self):
        return BarGraph()


class ConcretePie(Graph):
    def factory_method(self):
        return PieGraph()


class ConcreteScatter(Graph):
    def factory_method(self):
        return ScatterGraph()

# Contributors
# Product(ABC) = Grapy Type ABC
# Product1 = Concrete Bar class
# Product2 = Concrete Pie class
# Product3 = Concrete Scatter class
#
# Creator = Graph ABC class
# ConcreteCreator1 = Return Product1()
# ConcreteCreator2 = Return Product2()
# ConcreteCreator3 = Return Product3()
