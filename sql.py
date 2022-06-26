import sqlite3
connection = sqlite3.connect("database.db")

class sqlClass:
    def createTable(self):
        try:
            sqliteConnection = sqlite3.connect("database.db")
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")
            sqlite_create_table_query = '''CREATE TABLE SqliteDb_developers (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    email text NOT NULL UNIQUE,
                                    joining_date datetime,
                                    salary REAL NOT NULL);'''
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
            print("Connected to SQLite")
            sqlite_insert_with_param = """INSERT INTO SqliteDb_developers
                            (id, name, email, joining_date, salary) 
                            VALUES (?, ?, ?, ?, ?);"""

            data_tuple = (id, name, email, joinDate, salary)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            sqliteConnection.commit()
            print("Python Variables inserted successfully into SqliteDb_developers table")
            cursor.close()
        except sqlite3.Error as error:
            print("Failed to insert Python variable into sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

