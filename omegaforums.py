# Scraper of https://omegaforums.net/forums/private-watch-sales/
from random import betavariate
import requests
from bs4 import BeautifulSoup
from omegaforumsController import omegaforumsController
from gmail import Gmail

class omegaforums:
    def __init__(self, searchWords):
        self.words = searchWords
        self.db = omegaforumsController()
        self.db.createTable()
        self.gmail = Gmail()

    def update(self):
        # Get the website
        page = requests.get("https://omegaforums.net/forums/private-watch-sales/")
        # Create a soup object
        soup = BeautifulSoup(page.content, "html.parser")
        # Select the node with all posts
        containerItem = soup.find('ol', class_="discussionListItems")
        titles = containerItem.find_all("h3", attrs={"class": "title"})
        links = [title.find("a", attrs={"data-previewurl": True}) for title in titles] # this is called list comprehension

        oldPosts = 0
        for link in links:
            for word in self.words:
                if (word in link.text.lower()):
                    title = link.text.strip()
                    user = link.parent.parent.parent.parent['data-author']
                    url = "https://omegaforums.net/" + link['href']

                    if not self.db.checkDatabase(title, user):
                        self.db.insertVariableIntoTable(title=title, user=user, url=url)
                        self.gmail.sendEmail(forum='OF', title=title, user=user, url=url)
                    else:
                        #print(f"OF: {title} - email allready sent")
                        oldPosts += 1
        if (oldPosts > 0):
            print(f"OF: {oldPosts} emails allready sent") 