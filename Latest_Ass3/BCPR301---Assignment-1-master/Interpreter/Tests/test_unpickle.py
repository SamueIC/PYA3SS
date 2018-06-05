from ..database_local import DBLocal
from ..pickler import Pickler
from unittest import TestCase


class TestUnpickler(TestCase):

    def setUp(self):
        self.local = DBLocal()
        self.local.connect()
        self.local.create_table()
        self.maxDiff = None

    def tearDown(self):
        self.local.close()
        self.local = None

    def test_unpickle_dict(self):
        expected = {1: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 2445, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"},
                    2: {"IhD": "A2f3", "Gender": "Male", "Age": 23, "Sales": 2565, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"},
                    3: {"IjD": "Aa23", "Gender": "Female", "Age": 25, "Sales": 25, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"},
                    4: {"IgD": "A23", "Gender": "Female", "Age": 26, "Sales": 225, "BMI": "normal", "salary": 20,
                        "Birthday": "24/06/1995"}}
        pickle = Pickler.pickle_unpickle(expected)
        self.local.insert_dictionary(pickle)
        result = Pickler.pickle_unpickle(self.local.get_db())
        self.assertEqual(expected, result)









