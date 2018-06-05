from Interpreter.database_abstract import DatabaseAbstract
from sqlite3 import connect


# Wesley
class DBLocal(DatabaseAbstract):
    # Wesley
    def connect(self, connection=":memory:"):
        """ create object that connects to the local db
            :memory: can be used for a stored db on the ram
            instead of a file/file location"""
        self.connection = connect(connection)
        self.cursor = self.connection.cursor()

    # Wesley
    def insert_record(self, value):
        """Insert a single record into the local database"""
        self.cursor.execute("insert into employee(personal) values(?)", [value])

    # Wesley
    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = ?", key)

    # Wesley
    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
        self.cursor.execute("update employee set personal = ? where key = ?", record)

    # Wesley
    def create_table(self):
        """ Create a table that will be created in the local db
                    this will store the key and the persons pickled details"""
        # sqlite3 auto increment is defined as 1 word, not 2 as per usual
        sql = "Create table if not exists employee(empNo integer primary key autoincrement, personal text)"
        self.cursor.execute(sql)
