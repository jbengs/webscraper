import sqlite3
connection = sqlite3.connect("omegaforums.db")

class omegaforumsController:
    def __init__(self):
        self.sqliteConnection = sqlite3.connect("omegaforums.db")
        self.cursor = self.sqliteConnection.cursor()

    def createTable(self):
        try:
            query = """CREATE TABLE omegaforums (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                user TEXT NOT NULL,
                url TEXT NOT NULL);"""
            self.cursor.execute(query)
            self.sqliteConnection.commit()
        except sqlite3.Error as error:
            print("helloworld")
            print(error)

    def insertVariableIntoTable(self, title, user, url):
        titleLower = title.lower()
        userLower = user.lower()
        try:
            query = """INSERT INTO omegaforums
                                        (title, user, url)
                                        VALUES(?,?,?);"""
            data_tuple = (titleLower, userLower, url)
            self.cursor.execute(query, data_tuple)
            self.sqliteConnection.commit()
        except sqlite3.Error as error:
            print(f"Failed to insert {title} into sqlite omegaforums table: ", error)

    def checkDatabase(self, title, user):
        titleLower = title.lower()
        userLower = user.lower()
        try:
            query = """SELECT * FROM omegaforums WHERE
                    (title = ? AND user = ?)"""
            data_tuple = (titleLower, userLower)
            self.cursor.execute(query, data_tuple)
            rows = self.cursor.fetchone()
            self.sqliteConnection.commit()
            if rows is None:
                return False
            else:
                return True
        except sqlite3.Error as error:
            print("Failed to check omegaforums table. Error: ", error)

    def fetchDatabase(self):
        try:
            self.cursor.execute("SELECT * FROM omegaforums")
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)
            self.sqliteConnection.commit()
        except sqlite3.Error as error:
            print("Failed to fetchAll from omegaforums: ", error)
