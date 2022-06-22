# This is a code along of the turtorial "Beautiful Soup: Build a Web Scraper With Python"
# found on https://realpython.com/beautiful-soup-web-scraper-python/

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
#  it’s possible that you’ll also get some extra whitespace.
# Since you’re now working with Python strings, you can .strip() the superfluous whitespace. 
#for job_element in job_elements:
#    title_element = job_element.find("h2", class_="title")
 #   company_element = job_element.find("h3", class_="company")
  #  location_element = job_element.find("p", class_="location")
    #print(title_element.text.strip())
    #print(company_element.text.strip())
    #print(location_element.text.strip())
    #print()

# FILTERING
# Finding elements depending on their text content is a powerful way to filter your HTML response for specific information.
# Beautiful Soup allows you to use either exact strings or functions as arguments for filtering text in Beautiful Soup objects.
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
print(len(python_jobs)) # prints the length of the vector python_jobs

# Going up after filtering
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

# Printing all results
for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    #EXTRACT URL
    link_url = job_element.find_all("a")[1]['href'] #finds both links, then takes the seond one using [1]
    print(f"Apply here: {link_url}\n")
    print()

    # Finding the links to apply for jobs
    # links = job_element.find_all("a", string=lambda text: "apply" in text.lower())
    # for link in links:
    #    link_url = link["href"]
    #    print(f"Apply here: {link_url}\n")

  