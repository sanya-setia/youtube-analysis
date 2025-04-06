from datetime import timedelta
from dotenv import load_dotenv
from datetime import timedelta
from googleapiclient.discovery import build
import os
import re
load_dotenv()

#Adding our API Key safely
api_key = os.getenv('API_KEY')

#Building the service
youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlistItems().list(
    part="contentDetails",
    playlistId="PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB_"
    )

pl_response = pl_request.execute()
vid_ids = []
for item in pl_response['items']:
    vid_ids.append(item['contentDetails']['videoId'])

print(','.join(vid_ids))

vid_request = youtube.videos().list(
    part="contentDetails",
    id=','.join(vid_ids)
)

vid_response = vid_request.execute()

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern= re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

for item in vid_response['items']:
    duration = item['contentDetails']['duration']
    hours = hours_pattern.search(duration)
    minutes = minutes_pattern.search(duration)
    seconds = seconds_pattern.search(duration)
    
    hours = int(hours.group(1)) if hours else 0
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1)) if seconds else 0
    
    video_seconds = timedelta(
        hours= hours,
        minutes= minutes,
        seconds= seconds
    ).total_seconds()
    
    print(video_seconds)
    print()
