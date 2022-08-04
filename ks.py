#Scraper of klocksnack.se
import requests
from bs4 import BeautifulSoup
from ksController import ksController
from gmail import Gmail

class ks:
    def __init__(self, searchWords):
        self.db = ksController() # Connection to sqlite database
        self.db.createTable()    # Sets up database table
        self.gmail = Gmail()     # Sets up connection to Gmail API
        self.words = searchWords # Search words

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
                    # Find user element
                    userTag = link.parent.parent.find('ul', class_="structItem-parts").find('a', class_="username")
                    userId = userTag["data-user-id"]
                    userName = userTag.text.strip()
                    title = link.text.strip()
                    url = "https://klocksnack.se" + link['href']
                    # Check database if the post has allready been used
                    if not self.db.checkDatabase(title, userName):
                        self.db.insertVaribleIntoTable(title=title, user=userName, user_id=userId, url=url)
                        self.gmail.sendEmail(forum='KS', title=title, user=userName, url=url)
                    else:
                        print(f"KS: {title} - email allready sent")