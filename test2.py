print("Hello world from test2")

import requests
from bs4 import BeautifulSoup

result = requests.get("https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/")
src = result.content
soup = BeautifulSoup(src, 'html.parser')
links = soup.find_all('a')
print(soup.prettify)

for link in links:
    if "Omega" in link.text:
        print("success")
        print(link.text)
        print(link.attrs['href'])

