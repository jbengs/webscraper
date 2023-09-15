# Automated webscraper that emails any findings to subscribers.
This project was born out of my interest for the mechanical wonders that are vintage watches. As a collector, I need to constantly monitor the various watch forums that exists for possible aquisitions. As an engineer, I wanted to automate this.

This application is built to monitor the marketplace of [Klocksnack.se](https://klocksnack.se/forums/handla-s%C3%A4ljes-bytes.11/), a swedish watch forum.

The user specifies search criterieas through the command line. When the app discovers a new posting, it will send an email to the subscriber. The email contains a brief outline of the discovery, enough for the user to judge if its a true or false positive. A link to the full posting is included, so that the user can get full information with just one click. The app remembers any previous findings and will not send a new notification when a posting is bumped up.

Functionallity to scrape the German forum [Uhrform.de](https://uhrforum.de/forums/angebote.11/) and the American forum [Omegaforums.net](https://omegaforums.net/forums/private-watch-sales/) has been added.

## Tech Stack
This application is written in Python, with SQLite3 as database. Webscraping is done using the [Beautiful soup parser](https://beautiful-soup-4.readthedocs.io/en/latest/#) and the email service is provided via Gmail's API.

## Demo
The user specifies the search criteria and frequency by editing the file app.py. Subscribing email is edited in gmail.py.

![demo1](https://github.com/joelbengs/TheGoldDigger/blob/media/images/demo1.png?raw=true)

The application scans the forums for the set of keywords. Every post found is stored in the database and if it reappears in the forum, it will not trigger a new email.

![demo2](https://github.com/joelbengs/TheGoldDigger/blob/media/images/demo2.png?raw=true)

The subscriber recieve emails from the server.

![demo3](https://github.com/joelbengs/TheGoldDigger/blob/media/images/demo3.png?raw=true)

The user can access the finding through the link in the email.

![demo4](https://github.com/joelbengs/TheGoldDigger/blob/media/images/demo4.png?raw=true)

## How to use
    1. Download the files
    2. Open Powershell or the Terminal and navigate to the directory
    3. Set up a virtual environment in Python.
    4. Launch the virtual environment using the command "venv\Scripts\Activate.ps1" (on windows powershell) or "source venv/Scripts/activate.sh" on Mac.
    4. Install dependencies ("pip install google-auth google-auth-oauthlib google-api-python-client requests beautifulsoup4 gmail")
    6. Edit keywords and frequency in app.py. Edit subscriber email in gmail.py.
    5. Launch app.py by typing *python app.py* in the active virtual environment
    6. If it is the first time, you are prompted to log in to the google cloud project
        1. The login creates a token.json file, that is .gitignored.
        2. If you need to redo login, simply remove the token.json file
    7. The app scans Klocksnack (and other sites) every 10 minutes for the searchwords provided in app.py
    8. To modify searchwords, change app.py
    9. To modify reciever email, modify gmail.py

## Third party requirments
This application requiers a Gmail account and a Google cloud project with the Gmail API enabled. It uses OAuth client ID credentials.

Read more [here](https://developers.google.com/gmail/api/quickstart/python) or better eplained [here](https://www.javatpoint.com/gmail-api-in-python)

### Details
The cloud project is hosted on bengsklockserver account.

It is an application under testing, so users must be added via the dashboard to be able to log in.

To get a new login: delete the token.json file and restart the script "quickstart.py".

There has to be a valid credentials.json file in the working directory. You obtain this file from google cloud dashboard, rename it and move it.
Note: gmail only accepts the Gmail API, not SSL and SMTP as in most tutorials.

## Tutorial
The file realPythonTutorial is a code along of the tutorial [Beautiful Soup: Build a Web Scraper With Python](https://realpython.com/beautiful-soup-web-scraper-python/)

## App written on the road to Paris, 27/06/2022
from now to infinity:\
    *i love you and chocolate*\
end
