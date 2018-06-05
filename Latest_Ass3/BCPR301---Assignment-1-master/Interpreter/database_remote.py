from mysql.connector import connect, cursor
from Interpreter.database_abstract import DatabaseAbstract


# Wesley
class DBRemote(DatabaseAbstract):
    # sadly, Wesley, even I don't like this, breaks my soul
    # The default values need to be set so the ABC can still run
    def connect(self, host=None, user=None, password=None, db=None):
        """Use a list to connect to the remote server
            :param host is the host parameter for the remote server
            :param user is the user parameter for the remote server
            :param password is the needed password for the remote server
            :param db selects the database to be used
            This will connect to the remote server and allow access to read/write
            into the database"""
        self.connection = connect(host=host,
                                  user=user,
                                  password=password,
                                  db=db,
                                  raise_on_warnings=False)

        self.cursor = self.connection.cursor()

    # Wesley
    def insert_record(self, value):
        """Insert a single record into the local database"""
        sql = "insert into employee(personal) values(%(value)s)"
        val = {'value': value}
        self.cursor.execute(sql, val)

    # Wesley
    def delete_record(self, key):
        """Delete a single record that matches the key"""
        self.cursor.execute("delete from employee where key = %s", key)

    # Wesley
    def update_record(self, key, value):
        """Rewrite a record that already exists"""
        record = (value, key)
        self.cursor.execute("update employee set personal = %s where key = %s", record)

    def create_table(self):
        """ Create a table that will be created in the local db
                    this will store the key and the persons pickled details"""
        # sqlite3 auto increment is defined as 1 word, not 2 as per usual
        sql = "Create table if not exists employee(empNo integer auto_increment primary key, personal blob)"
        self.cursor.execute(sql)

