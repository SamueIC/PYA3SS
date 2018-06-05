from Interpreter.database_handler import DatabaseHandler
from unittest import TestCase


# Wesley
class TestDBHandler(TestCase):
    # Wesley
    def setUp(self):
        self.handler = DatabaseHandler()
        self.handler.set_local("TestingPurpose")
        self.handler.set_remote("localhost", "root", "", "test")

    # Wesley
    def tearDown(self):
        self.handler.drop_local_table()
        self.handler.drop_remote_table()
        self.handler = None

    # Wesley
    def test_remote_insert_values(self):
        expected = {1: {"item": 'dskjhflkasdjlfkj23543'}, 2: {"item2": 'dskjhflkasdjlfkj23543'}}
        data = {0: {"item": 'dskjhflkasdjlfkj23543'}, 1: {"item2": 'dskjhflkasdjlfkj23543'}}
        self.handler.insert_remote_dict(data)
        result = self.handler.get_remote()
        self.assertEqual(expected, result)

    # Wesley
    def test_local_insert_values(self):
        expected = {1: {"item": 'dskjhflkasdjlfkj23543'}, 2: {"item2": 'dskjhflkasdjlfkj23543'}}
        data = {0: {"item": 'dskjhflkasdjlfkj23543'}, 1: {"item2": 'dskjhflkasdjlfkj23543'}}
        self.handler.insert_local_dict(data)
        result = self.handler.get_local()
        self.assertEqual(expected, result)

    # Wesley
    def test_remote_get(self):
        expected = {1: {"item": 'dskjhflkasdjlfkj23543'}, 2: {"item2": 'dskjhflkasdjlfkj23543'}}
        data = {0: {"item": 'dskjhflkasdjlfkj23543'}, 1: {"item2": 'dskjhflkasdjlfkj23543'}}
        self.handler.insert_remote_dict(data)
        result = self.handler.get_remote()
        self.assertEqual(expected, result)

    # Wesley
    def test_local_get(self):
        expected = {1: {"item": 'dskjhflkasdjlfkj23543'}, 2: {"item2": 'dskjhflkasdjlfkj23543'}}
        data = {0: {"item": 'dskjhflkasdjlfkj23543'}, 1: {"item2": 'dskjhflkasdjlfkj23543'}}
        self.handler.insert_local_dict(data)
        result = self.handler.get_local()
        self.assertEqual(expected, result)
