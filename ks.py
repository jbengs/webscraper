#Scraper of klocksnack.se

import requests
from bs4 import BeautifulSoup

page = requests.get("https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/")

soup = BeautifulSoup(page.content, "html.parser")

structItemContainer = soup.find(class_="structItemContainer-group js-threadList")

firstItem = structItemContainer.find('div')

structItems = firstItem.next_siblings

print(structItems)

#Constainer of all ads: class="structItemContainer-group js-threadList"