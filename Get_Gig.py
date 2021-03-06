from __future__ import print_function
import httplib2
import os

from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from config import google_calendar_id
import datetime

try:	
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = none
	
	
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json


SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)

    return credentials

def main():
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    eventsResult = service.events().list(
        calendarId= google_calendar_id, timeMin=now, maxResults=10,
    singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    this_week = datetime.date.today().isocalendar()[1]
    
    week_gigs = []

    if not events:
        pass
    for event in events:
        date = event['start'].get('date')
        year, month, day = (int(x) for x in date.split('-'))    
        dow = datetime.date(year, month, day).weekday()
        week = datetime.date(year, month, day).isocalendar()[1]
        day_name = datetime.date(year, month, day).strftime('%A')
        gig_sum = (event["summary"], dow, day_name)
        if week == this_week:
            week_gigs.append(gig_sum)
        else:
            continue
    
    return week_gigs


#if __name__ == '__main__':
#    main()
