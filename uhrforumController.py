import sqlite3
connection = sqlite3.connect("uhrforum.db")

class uhrforumController:
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
        titleLower = title.lower()
        userLower = user.lower()
        try:
            sqlite_insert_with_param = """INSERT INTO uhrforum
                            (title, user, user_id, url) 
                            VALUES (?, ?, ?, ?);"""
            data_tuple = (titleLower, userLower, user_id, url)
            self.cursor.execute(sqlite_insert_with_param, data_tuple)
            self.sqliteConnection.commit()
            #print(f"{title} inserted successfully into uhrforum table")
        except sqlite3.Error as error:
            print(f"Failed to insert {title} into sqlite uhrforum table: ", error)

    # Checks wheter the row allready exist in the database. Returns True if it exists, else False
    def checkDatabase(self, title, user):
        titleLower = title.lower()
        userLower = user.lower()
        try:
            query = """SELECT * FROM uhrforum WHERE
                        (title = ? AND user = ?)"""
            data_tuple = (titleLower, userLower)
            self.cursor.execute(query, data_tuple)
            rows = self.cursor.fetchone()
            self.sqliteConnection.commit()
            if not rows is None:
                #print(f'TRUE: {title} by user {user} exist in uhrforum table')
                return True
            else:
                #print(f'False: {title} by user {user} exist in uhrforum table: False')
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
