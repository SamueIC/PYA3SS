from ..pickler import Pickler
from unittest import TestCase


# Wesley
class TestPicklerSetUp(TestCase):
    def setUp(self):
        self.pickler = Pickler()

    def tearDown(self):
        self.pickler = None

    def test_pickle_dictionary_type_byte(self):
        """True if all values in dictionary are of type 'byte'"""
        expected = bytes
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        data = self.pickler.pickle_unpickle(data)
        result = (type(value) == expected for value in data.values())
        self.assertTrue(all(result))

    def test_pickle_dictionary_type_string(self):
        """False if any values in dictionary are of type 'string'"""
        the_type = bytes
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        data = self.pickler.pickle_unpickle(data)
        data[2] = "This is a string"
        result = (type(value) == the_type for value in data.values())
        self.assertFalse(all(result))

    def test_pickle_dictionary_type_string_true(self):
        """True if a value in dictionary are of type 'string'"""
        the_type = str
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        data = self.pickler.pickle_unpickle(data)
        data[2] = "This is a string"
        result = (type(value) == the_type for value in data.values())
        self.assertTrue(any(result))

