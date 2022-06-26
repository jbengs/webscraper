#Scraper of klocksnack.se
import requests
from bs4 import BeautifulSoup
import sqlite3
connection = sqlite3.connect("database.db")

# Prints how many rows we have changed in the database this session.
print(connection.total_changes)
# Cursor objects allow us to send SQL statements to a SQLite database using cursor.execute().
db = connection.cursor()
db.execute("DROP TABLE klocksnack")
db.execute("CREATE TABLE klocksnack (title VARCHAR PRIMARY KEY)")
db.execute("INSERT INTO klocksnack (title) VALUES ('testString')")
print("testprint from database\n")
print(db.execute("SELECT title FROM klocksnack").fetchall())

# Get the website
page = requests.get("https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/")

# Create a soup object
soup = BeautifulSoup(page.content, "html.parser")

# Select the div with all posts
allItems = soup.find(class_="structItemContainer-group js-threadList")

# Searches all tags looking for links <a> that has both "href" and "data-preview-url" attributes. 
# Some attributes, like the data-* attributes in HTML 5, have names that can’t be used as the names of keyword arguments:You can use these attributes in searches by putting them into a dictionary and passing the dictionary into find_all() as the attrs argument:
links = allItems.find_all("a", attrs={"href":True, "data-preview-url":True})

# Search words in lower case
words = ["omega","cartier", "rolex"]

# Set of allready found ones

# Iterate the links and check all search words
# for link in links:
#     for word in words:
#         if(word in link.text.lower()):

#             query = """INSERT INTO klocksnack (title) VALUES (?,);"""
#             title = link.text.strip()
#             data_tuple = (title,) #the comma is needed to make it a tuple
                      
#             db.execute(query, data_tuple)
#             db.commit()

#             print(link)
#             print(title)
#             print()


def insertVaribleIntoTable(id, name, email, joinDate, salary):
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

insertVaribleIntoTable(2, 'Joe', 'joe@pynative.com', '2019-05-19', 9000)
insertVaribleIntoTable(3, 'Ben', 'ben@pynative.com', '2019-02-23', 9500)    

#print(list(filteredLinks))

# for item in allItems.children:
#     main = item.find('div', class_='structItem-cell structItem-cell--main')
#     title = main.find('div', class_='structItem-title')
#     link_url = title.find_all('a')[1]['href']
#     print(f"the watch here: {link_url}\n")
#     print()


# finds all the other posts as an iterable
#structItems = firstItem.find_next_siblings

#print(type(structItems))

#for item in firstItem.find_next_siblings:
# main = item.find('div', class_='structItem-cell structItem-cell--main')
# title = main.find('div', class_='structItem-title')
# link_url = title.find_all('a')[1]['href']
# print(f"the watch here: {link_url}\n")
# print()

#Constainer of all ads: class="structItemContainer-group js-threadList"