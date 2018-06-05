from database_remote import DBRemote
from unittest import TestCase


# Wesley
class TestPicklerSetUp(TestCase):
    # Wesley
    def setUp(self):
        self.db = DBRemote()
        self.db.connect("testing")
        self.db.create_table()

    # Wesley
    def tearDown(self):
        self.db.drop_table()
        self.db.close()
        self.db = None

    # Wesley
    def test_db_insert_values(self):
        """Create a table, insert graph_data and check the return graph_data is what was inserted"""
        expected = [(1, 'dskjhflkasdjlfkj23543'), (2, 'dskjhflkasdjlasdfdsafkj23543')]
        self.db.insert_record("dskjhflkasdjlfkj23543")
        self.db.insert_record("dskjhflkasdjlasdfdsafkj23543")
        self.db.commit()
        result = self.db.get_db()
        self.assertEqual(expected, result)




