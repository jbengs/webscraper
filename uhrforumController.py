import sqlite3
connection = sqlite3.connect("uhrforum.db")

class ksController:
    def __init__(self):
        self.sqliteConnection = sqlite3.connect("uhrforum.db")
        self.cursor = self.sqliteConnection.cursor()

    def createTable(self):
        try:
            query= """CREATE TABLE uhrforum (
                                    id INTEGER PRIMARY KEY,
                                    title TEXT NOT NULL,
                                    user text NOT NULL,
                                    user_id INTEGER NOT NULL,
                                    url TEXT NOT NULL);"""
            self.cursor.execute(query)
            self.sqliteConnection.commit()
            print("SQLite table 'uhrforum' created")
        except sqlite3.Error as error:
            #print("Failed to create sqlite table uhrforum. Error: ", error)
            print(error)
            
    def insertVaribleIntoTable(self, title, user, user_id, url):
        try:
            sqlite_insert_with_param = """INSERT INTO uhrforum
                            (title, user, user_id, url) 
                            VALUES (?, ?, ?, ?);"""
            data_tuple = (title, user, user_id, url)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.sqliteConnection.commit()
            #print(f"{title} inserted successfully into klocksnack table")
        except sqlite3.Error as error:
            print(f"Failed to insert {title} into sqlite uhrforum table: ", error)

    # Checks wheter the row allready exist in the database. Returns True if it exists, else False
    def checkDatabase(self, title):
        try:
            query = """SELECT (title) FROM uhrforum WHERE
                        (title = ?)"""
            data_tuple = (title,)
            self.cursor.execute(query, data_tuple)
            rows = self.cursor.fetchone()
            self.sqliteConnection.commit()
            if not rows is None:
                #print(f'{title} exist in klocksnack table: True')
                return True
            else:
                #print(f'{title} exist in klocksnack table: False')
                return False
        except sqlite3.Error as error:
            print("Failed to check uhrforum table. Error: ", error)

    def fetchDatabase(self):
        try:
            self.cursor.execute("SELECT * FROM uhrforum")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.sqliteConnection.commit()
        except sqlite3.Error as error:
            print("Failed to fetchAll from uhrforum: ", error)
