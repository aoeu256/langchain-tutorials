import google.auth, pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# First, authenticate with Google using OAuth2 credentials
creds = None
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = google.auth.default(scopes=['https://www.googleapis.com/auth/keep'])
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# Build the Google Keep API client
service = build('keep', 'v1', credentials=creds)

# Create a new note with the message "Hello world!"
note = {
    "title": "My Note",
    "text": "Hello world!"
}
created_note = service.notes().create(body=note).execute()

# Print the ID of the newly created note
print("Note created with ID:", created_note['name'][5:])