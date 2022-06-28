#Scraper of klocksnack.se
import requests
from bs4 import BeautifulSoup
from ksController import ksController
from mail import Mail

class ks:
    def __init__(self, searchWords):
        # Create the database
        self.db = ksController()
        self.db.createTable()
        self.mail = Mail()
        self.words = searchWords

    def update(self):
        # Get the website
        page = requests.get("https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/")
        # Create a soup object
        soup = BeautifulSoup(page.content, "html.parser")
        # Select the div with all posts
        allItems = soup.find(class_="structItemContainer-group js-threadList")
        # Searches all tags looking for links <a> that has both "href" and "data-preview-url" attributes. 
        # Some attributes, like the data-* attributes in HTML 5, have names that can’t be used as the names of keyword arguments:You can use these attributes in searches by putting them into a dictionary and passing the dictionary into find_all() as the attrs argument:
        links = allItems.find_all("a", attrs={"href":True, "data-preview-url":True})

        #Iterate the links and check all search words
        for link in links:
            for word in self.words:
                if(word in link.text.lower()):
                    userTag = link.parent.parent.find('ul', class_="structItem-parts").find('a', class_="username")
                    userId = userTag["data-user-id"]
                    userName = userTag.text.strip().lower()
                    title = link.text.strip().lower()
                    url = "https://klocksnack.se2" + link['href']
                    if not self.db.checkDatabase(title):
                        self.db.insertVaribleIntoTable(title=title, user=userName, user_id=userId, url=url)
                        print("mail.send('KS',title, userName, url")
                    else:
                        print("dont send email")
                    
                    # print()
                    # print(title)
                    # print(url)
                    # print('userlink: ')
                    # print(userTag)
                    # print('user: ')
                    # print(userName)
                    # print('userId: ')
                    # print(userId)