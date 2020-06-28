from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
from datetime import datetime
import os
import threading

class Upload(threading.Thread):
    def __init__(self, event_upload, base_path):
        self.event_upload = event_upload
        self.base_path = base_path
        self.output_dir = os.path.join(base_path, 'outputs')
        self.data_dir = os.path.join(base_path, 'data')
        # If modifying these scopes, delete the file token.pickle.
        self.scopes = ['https://www.googleapis.com/auth/drive.file'] #defines permissions

        self.creds = None

        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        token_path = os.path.join(self.data_dir, 'token.pickle')
        if os.path.exists(token_path):
            with open(token_path, 'rb') as token:
                self.creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            cred_path = os.path.join(self.data_dir, 'credentials.json')
            if os.path.isfile(cred_path):
                print("Credentials file found")
            else:
                print("No credentials found")

            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        cred_path, self.scopes)
                    self.creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open(token_path, 'wb') as token:
                    pickle.dump(self.creds, token)

        print(datetime.now())

    def File_Upload(self):
        self.event_upload.wait()
        if not os.listdir(self.output_dir):
            print("No files in directory")
            return
        service = build('drive', 'v3', credentials=self.creds)
        self.file = os.path.join(self.output_dir, 'video.avi')
        folder_ID = '1Qcfxg48V4nJpKwU4_1oSoEs0jUrrt0EZ'
        file_metadata = {
        'name': f'{datetime.now()}.avi',
        'parents': [folder_ID]
        }
        media = MediaFileUpload(self.file,
                                mimetype='video/avi',
                                resumable=True)
        self.file = service.files().create(body=file_metadata,
                                            media_body=media,
                                            fields='id').execute()

        self.event_upload.clear()

    def Get_FileID(self):
        print('File ID: %s' % self.file.get('id'))

    def __exit__(self):
        print("Exiting")
        for files in os.listdir(self.output_dir):
            print("Files:", files)
            file_path = os.path.join(self.output_dir, files)
            #path = f"{os.getcwd()}/Outputs/{files}"
            if file_path.endswith(".gitignore"):
                pass
            else:
                os.remove(file_path)

if __name__ == '__main__':
    up = Upload("/home/pi/Documents/Python/CatBerry")
    up.File_Upload()
    up.Get_FileID()
    up.__exit__()