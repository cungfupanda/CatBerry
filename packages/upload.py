from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from datetime import datetime
import os

class Upload(object):
    def __init__(self):
        # If modifying these scopes, delete the file token.pickle.
        self.scopes = ['https://www.googleapis.com/auth/drive.file'] #defines permissions

        self.creds = None

        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        '/home/pi/Documents/Python/CatPie/credentials.json', self.scopes)
                    self.creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(self.creds, token)

        print(datetime.now())

    def File_Upload(self, file):
        if not os.listdir('Outputs'):
            print("No files in directory")
            return
        service = build('drive', 'v3', credentials=self.creds)
        self.file = file
        folder_ID = '1Qcfxg48V4nJpKwU4_1oSoEs0jUrrt0EZ'
        file_metadata = {
        'name': f'{datetime.now()}.mp4',
        'parents': [folder_ID]
        }
        media = MediaFileUpload(self.file,
                                mimetype='video/mp4',
                                resumable=True)
        self.file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()

    def Get_FileID(self):
        print('File ID: %s' % self.file.get('id'))

    def __exit__(self):
        print("Exiting")
        for files in os.listdir('Outputs'):
            print("Files:", files)
            path = f"{os.getcwd()}/Outputs/{files}"
            os.remove(path)

if __name__ == '__main__':
    up = Upload()
    up.File_Upload('Outputs/video.mp4')
    up.Get_FileID()
    up.__exit__()