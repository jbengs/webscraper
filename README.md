# webscraper
A webscraper built to scrape Klocksnack

## Third party requirments
This application requiers an gmail account and a Google cloud project with the gmail API enabled. Part of this is the use of OAuth client ID credentials.

Read more here: https://developers.google.com/gmail/api/quickstart/python
OR better eplained here: https://www.javatpoint.com/gmail-api-in-python

### Details
The cloud project is hosted on bengsklockserver account.
It is an application under testing, so users mus be added via the dashboard to be able to log in.
To get a new login: delete the token.json file and restart the script "quickstart.py". There has to be a valid credentials.json file in the working directory. You obtain this file from google cloud dashboard, rename it and move it.
Note: gmail only accepts the Gmail API, not SSL and smtp

## Security
The communication with Google is SSL encrypted. The user inputs password upon start

## Tutorial
The file realPythonTutorial is aa code along of the tutorial "Beautiful Soup: Build a Web Scraper With Python" found on https://realpython.com/beautiful-soup-web-scraper-python/

### App written on the road to Paris, 27/06/2022
for now to infinity:
    i love you and chocolate
end