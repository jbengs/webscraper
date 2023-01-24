# webscraper
A webscraper built to scrape the marketplace of Klocksnack.se, a swedish watch forum. Functionallity to scrape the german forum Uhrform.de and the american forum omegaforums.net has been added.

## How to use
    1. Download the files
    2. Open powershell and navigate to the directory
    3. Set up a virtual environment in python using the command "venv\Scripts\Activate.ps1".
    4. Install dependencies
    5. Launch app.py by typing *python app.py* in the active virtual environment
    6. If it is the first time, you are prompted to log in to the google cloud project
        1. The login creates a token.json file, that is .gitignored
        2. If you need to redo login, simply remove the token.json file
    7. The app scans Klocksnack (and other sites) every 10 minutes for the searchwords provided in app.py
    8. To modify searchwords, change app.py
    9. To modify reciever email, modify gmail.py

## Third party requirments
This application requiers a Gmail account and a Google cloud project with the Gmail API enabled. It uses OAuth client ID credentials.

Read more here: https://developers.google.com/gmail/api/quickstart/python \
OR better eplained here: https://www.javatpoint.com/gmail-api-in-python

### Details
The cloud project is hosted on bengsklockserver account.\
It is an application under testing, so users must be added via the dashboard to be able to log in.\
To get a new login: delete the token.json file and restart the script "quickstart.py".\
There has to be a valid credentials.json file in the working directory. You obtain this file from google cloud dashboard, rename it and move it.\
Note: gmail only accepts the Gmail API, not SSL and SMTP as in most tutorials.\

## Tutorial
The file realPythonTutorial is a code along of the tutorial "Beautiful Soup: Build a Web Scraper With Python" found on\ https://realpython.com/beautiful-soup-web-scraper-python/

### App written on the road to Paris, 27/06/2022
from now to infinity:\
    *i love you and chocolate*\
end
