import imp
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
# requests library has method for HTTP requests
page = requests.get(URL)

# The page.text is a text representation of the actual content of the response: page.content
# print(page.text)

# BeautifulSoup is a library that brings structure to things, such as a HTML DOM.
soup = BeautifulSoup(page.content, "html.parser")

# Here we identify the div containing what we are looking for, and it has the id "ResultsContainer"
results = soup.find(id="ResultsContainer")

# With BS you can prettify the html before printing
# print(results.prettify)

# We know lift out all divs with the class card-content. find_all returns an iterable
job_elements = results.find_all("div", class_="card-content")

# for job_element in job_elements:
#    print(job_element, end="\n"*2)

# We then single out the relevant information for each job post
# You can add .text to a Beautiful Soup object to return only the text content of the HTML elements that the object contains:
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()