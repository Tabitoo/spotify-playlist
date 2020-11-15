from googleapiclient.discovery import build
import json
import youtube_dl

key = 'AIzaSyDIk_jiykq54JAWso0RJ0aHP5Q6W2g5CyI'


youtube = build('youtube', 'v3', developerKey=key)

request = youtube.channels().list(part='contentDetails', forUsername="tabitoo")


channelId = "UCeBxA7b4S5D4UrZ7izo9-Mg"

#print(channelId)

idKey = "UCeBxA7b4S5D4UrZ7izo9-Mg"
idplay = 'PLcLboY1OgBHktpUSTeZ539VmT3UgEszZc'

reques2  = youtube.playlists().list(
    part='contentDetails, snippet',
    channelId=idKey
)

reques3  = youtube.playlistItems().list(
    part='snippet',
    playlistId=idplay
)

"""
url = 'https://www.youtube.com/watch?v=eJnQBXmZ7Ek'


ydl = YoutubeDL()

with ydl:
    video = ydl.extract_info(url, download=False)


print('{} - {}'.format(video['artist'], video['track']))
"""

url = "https://www.youtube.com/watch?v=F8c8f2nK82w"
video = youtube_dl.YoutubeDL({}).extract_info(url, download=False, extra_info={})


song = video["track"]
artist = video["artist"]

#playlistList = reques2.execute()
#playlistitems = reques3.execute()

#print(playlistitems)
#print(playlistList['items'][0]['snippet']['title'])

"""
for items in playlistList['items']:
    print(items)
    print()

for items in playlistList['items']:
    print(items['snippet']['title'])
    print()

"""

