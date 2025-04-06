import os
from dotenv import load_dotenv
load_dotenv()
from googleapiclient.discovery import build

#Adding our API Key safely
api_key = os.getenv('API_KEY')

#Building the service
youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels  ().list(
    part='contentDetails',
    forUsername='schafer5'
    )

response = request.execute()

print(response)
