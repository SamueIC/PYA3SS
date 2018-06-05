from unittest import TestCase
from Interpreter.chart import Graph, PieGraph, ScatterGraph, BarGraph


class TestCharts(TestCase):
    # Wesley
    def test_set_criteria(self):
        a = Graph()
        data = {0: {"1D": "A231", "Gender": "F", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1994"},
                1: {"ID": "B324", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"},
                2: {"ID": "C322", "Gender": "M", "Age": "26", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1991"},
                3: {"ID": "D032", "Gender": "M", "Age": "27", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1990"}}
        a.set_data(data, 'bar', 'data2.txt')
        a.set_criteria("Gender", 'Female')

        # a.set_data({"dfd": "asdfds"}, "bar", "C:\\temp\\random.html")
        # a.graph_data = {0: {"ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
        #                        "Birthday": "24/06/1995"}}

        a.graph_type.set_data_keys("Gender", "Sales")
        expected = "F"
        actual = a.graph_type.data[0]['Gender']
        self.assertEqual(expected, actual)






