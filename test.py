import requests
from bs4 import BeautifulSoup

result = requests.get("https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/")
src = result.content
soup = BeautifulSoup(src)
#links = soup.find_all("a")
#print(links)

"""
for link in links
    if "Omega" in link.text:
        print(link)
        print(link.attrs['href'])
"""
