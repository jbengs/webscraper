#Scraper of klocksnack.se

import requests
from bs4 import BeautifulSoup

# Get the website
page = requests.get("https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/")

# Create a soup object
soup = BeautifulSoup(page.content, "html.parser")

# Select the div with all posts
structItemContainer = soup.find(class_="structItemContainer-group js-threadList")

# Select the first post div
firstItem = structItemContainer.find('div')

# finds all the other posts as an iterable
structItems = firstItem.find_next_siblings

print(type(structItems))

for item in structItems:
    main = item.find('div', class_='structItem-cell structItem-cell--main')
    title = main.find('div', class_='structItem-title')

#Constainer of all ads: class="structItemContainer-group js-threadList"