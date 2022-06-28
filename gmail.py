from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from email.message import EmailMessage
import base64

class Gmail:

    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        self.SCOPES = ['https://mail.google.com/']
        self.getCreds() # to make self.creds refer to the token.json file
        
    def getCreds(self):
        self.creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.creds.to_json())

    def listLabels(self):
        try:
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=self.creds)
            results = service.users().labels().list(userId='me').execute()
            labels = results.get('labels', [])
            if not labels:
                print('No labels found.')
                return
            print('Labels:')
            for label in labels:
                print(label['name'])

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f'An error occurred: {error}')

    def sendEmail(self, forum, title, user, url):
        try:
            service = build('gmail', 'v1', credentials=self.creds)
            
            # prepare message
            signature = "Always at your service,\nbengsklockservice"
            message = EmailMessage()
            message.set_content(f'{title} was just posted on {forum} by {user}\n{url}\n\n{signature}')
            message['To'] = 'bengs.joel@gmail.com'
            message['From'] = 'bengsklockserver@gmail.com'
            message['Subject'] = f'{forum}: {title}'

            # encoded message
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                .decode()

            # create message
            create_message = {
                'raw': encoded_message
            }
            
            # send
            send_message = (service.users().messages().send
                            (userId="me", body=create_message).execute())
            print(F'Message Id: {send_message["id"]}')
        except HttpError as error:
            print(F'An error occurred: {error}')
            send_message = None
        return send_message