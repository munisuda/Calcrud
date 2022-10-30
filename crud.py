from curses.ascii import NUL
from datetime import datetime, timedelta
from pickle import GLOBAL
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

load_dotenv()


flow = InstalledAppFlow.from_client_secrets_file("og-creds.json", scopes=os.environ.get('SCOPES'))


def inserter(year: int,month:int ,day:int ,hour_24: int,min:int,summary:str,location:str, description:str, time_before_email :int,time_before_popup: int):
  starttime = datetime(year,month,day,hour_24,min)
  endtime = starttime + timedelta(minutes=60)
  event = {
  'summary': summary,
  'location': location,
  'description': description,
  'start': {
    'dateTime': starttime.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': os.environ.get('timezone'),
  },
  'end': {
    'dateTime': endtime.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': os.environ.get('timezone'),
  },
  'attendees': [{
    "email":"someone@something.com"
  }],
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes':time_before_email},
      {'method': 'popup', 'minutes': time_before_popup},
    ],
  },
}

  credentials = flow.run_console()
  service = build("calendar", 'v3', credentials=credentials)
  event = service.events().insert(calendarId=os.environ.get('calID'), body=event).execute()
  print('Event created: %s' % (event.get('htmlLink')))
  global eventID
  eventID = event['id']
  print("The event ID is " + eventID)