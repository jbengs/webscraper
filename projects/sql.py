import sqlite3
connection = sqlite3.connect("database.db")

class sqlClass:
    def __init__(self):
        self.sqliteConnection = sqlite3.connect("database.db")
        self.cursor = self.sqliteConnection.cursor()

    def createTable(self):
        try:
            query= """CREATE TABLE myTable (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);"""
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            print("SQLite table created")
        except sqlite3.Error as error:
            print("Failed to create sqlite table", error)

    def insertVaribleIntoTable(self, id, name, email, joinDate, salary):
        try:
            sqlite_insert_with_param = """INSERT INTO myTable
                            (id, name, email, joining_date, salary) 
                            VALUES (?, ?, ?, ?, ?);"""
            data_tuple = (id, name, email, joinDate, salary)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.sqliteConnection.commit()
            print("Python Variables inserted successfully into myTable table")
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)

    # Checks wheter the row allready exist in the database. Returns True if it exists, else False
    def checkDatabase(self, id):
        try:
            query = "SELECT id FROM myTable WHERE id = ?"
            data_tuple = (id,)
            self.cursor.execute(query, data_tuple)
            rows = self.cursor.fetchone()
            self.sqliteConnection.commit()
            if not rows is None:
                print(f'id {id} exist in myTable: True')
                return True
            else:
                print(f'id {id} exist in myTable: False')
                return False
        except sqlite3.Error as error:
            print("Failed to check sqlite table. Error: ", error)

    def fetchDatabase(self):
        try:
            self.cursor.execute("SELECT * FROM myTable")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.sqliteConnection.commit()
        except sqlite3.Error as error:
            print("Failed to fetchAll from myTable: ", error)
