import sqlite3
connection = sqlite3.connect("database.db")


class sqlClass:

    #def __init__(self):
     #   sqliteConnection = sqlite3.connect("database.db")
      #  self.cursor = sqliteConnection.cursor()

    def createTable(self):
        try:
            sqliteConnection = sqlite3.connect("database.db")
            cursor = sqliteConnection.cursor()
            sqlite_create_table_query = """CREATE TABLE myTable (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);"""
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to create sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()

    def insertVaribleIntoTable(self, id, name, email, joinDate, salary):
        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            sqlite_insert_with_param = """INSERT INTO myTable
                            (id, name, email, joining_date, salary) 
                            VALUES (?, ?, ?, ?, ?);"""
            data_tuple = (id, name, email, joinDate, salary)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into myTable table")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()

    def checkDatabase(self, id):
        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            sqlite_select_with_param = "SELECT id FROM myTable WHERE id = 20;"
            #data_tuple = (id,)
            rows = cursor.execute(sqlite_select_with_param)
            sqliteConnection.commit()
            print("Python Variables checked from myTable table")
            
            if rows:
                cursor.close()
                print("Returned True")
                return True
            else:
                print ("returned False")
                cursor.close()
                return False
        except sqlite3.Error as error:
            print("Failed to check Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()

    def fetchDatabase(self):
        try:
            sqliteConnection = sqlite3.connect('database.db')
            cursor = sqliteConnection.cursor()
            cursor.execute("SELECT * FROM myTable")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            sqliteConnection.commit()
            print("Python Variables checked from myTable table")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to fetchAll from myTable: ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
