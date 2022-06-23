#Scraper of klocksnack.se

import requests
from bs4 import BeautifulSoup

# Get the website
page = requests.get("https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/")

# Create a soup object
soup = BeautifulSoup(page.content, "html.parser")

# Select the div with all posts
allItems = soup.find(class_="structItemContainer-group js-threadList")

# Searches all tags looking for links <a> that has both "href" and "data-preview-url" attributes. 
# Some attributes, like the data-* attributes in HTML 5, have names that can’t be used as the names of keyword arguments:You can use these attributes in searches by putting them into a dictionary and passing the dictionary into find_all() as the attrs argument:
links = allItems.find_all("a", attrs={"href":True, "data-preview-url":True})
links_soup = BeautifulSoup(links, "html.parser")
omegalinks = links_soup.find_all("a", string=lambda text: "omega" in text.lower())


for link in omegalinks:
    print(link.text.strip())
    
#filteredLinks = filter(lambda text: "omega" in text.lower(), links)

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