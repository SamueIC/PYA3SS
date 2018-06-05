from abc import ABCMeta, abstractmethod


# Wesley
class DatabaseAbstract(metaclass=ABCMeta):
    # Wesley
    def __init__(self):
        self.connection = None
        self.cursor = None

    # Wesley
    @abstractmethod
    def connect(self):
        pass

    # Wesley
    @abstractmethod
    def create_table(self):
        pass

    # Wesley
    def drop_table(self):
        """Used for testing, will drop table to clear graph_data"""
        self.cursor.execute("Drop table if exists employee")

    # Wesley
    def insert_dictionary(self, dictionary):
        """Write a dictionary with key and pickled values
            into the database"""
        for key, value in dictionary.items():
            self.insert_record(value)

    # Wesley
    def get_db(self):
        """Return the database"""
        self.cursor.execute("select empNo, personal from employee")
        return self.cursor.fetchall()

    # Wesley
    def commit(self):
        """Changes to the database need to be committed to the database"""
        self.connection.commit()

    # Wesley
    def close(self):
        """Close the connection after each crud operation with database"""
        self.connection.close()

    # Wesley
    def query(self, sql):
        """Test query"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # Wesley
    @abstractmethod
    def insert_record(self, value):
        pass

    # Wesley
    @abstractmethod
    def delete_record(self, key):
        pass

    # Wesley
    @abstractmethod
    def update_record(self, key, value):
        pass

