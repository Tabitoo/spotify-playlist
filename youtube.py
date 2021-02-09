from googleapiclient.discovery import build
import json
import youtube_dl

key = 'AIzaSyDIk_jiykq54JAWso0RJ0aHP5Q6W2g5CyI'


youtube = build('youtube', 'v3', developerKey=key)
#???? 
request = youtube.channels().list(part='contentDetails', forUsername="tabitoo")


channelId = "UCeBxA7b4S5D4UrZ7izo9-Mg"

#print(channelId)

idKey = "UCeBxA7b4S5D4UrZ7izo9-Mg"
idplay = 'PLcLboY1OgBHktpUSTeZ539VmT3UgEszZc'
#Reques2 se usa para obtener el id de la playlist que queremos
#para que el usuario pueda seleccionar una de sus playlist, hace un condicional(que verifique que el nombre es igual a x playlist) que itere sobre cada playlist
reques2  = youtube.playlists().list(
    part='contentDetails, snippet', 
    channelId=idKey
)

reques3  = youtube.playlistItems().list(
    part='snippet, id',
    playlistId=idplay,
    maxResults= 100,
)

"""
url = 'https://www.youtube.com/watch?v=eJnQBXmZ7Ek'


ydl = YoutubeDL()

with ydl:
    video = ydl.extract_info(url, download=False)


print('{} - {}'.format(video['artist'], video['track']))
"""



"""url = "https://www.youtube.com/watch?v=mAcQRgPWZDE"
video = youtube_dl.YoutubeDL({}).extract_info(url, download=False, extra_info={})


song = video["track"]
artist = video["artist"]


print(song)
print(artist)
"""
"""
playlistList = reques2.execute()
playlistitems = reques3.execute()

print(playlistitems)
"""
#forma de llegar al titulo de una playlist
#print(playlistList['items'][0]['snippet']['title'])
#print(request)
"""
codigo = 'temas'

for nombres in playlistList['items']:
    if nombres['snippet']['title'] == 'temas':
        print(nombres['id'])
        break
else:
    print('no se encontro esa playlist')

print(playlistList)
"""
"""
lista = []
songs = []
artists = []

for items in playlistitems['items']:
    lista.append(items['snippet']['resourceId']['videoId'])


print(lista)

for videoId in lista:
    url = "https://www.youtube.com/watch?v=" + videoId
    video = youtube_dl.YoutubeDL({}).extract_info(url, download=False, extra_info={})
    songs.append(video["track"])
    artists.append(video["artist"])


for coso in artists:
    print(coso)

"""

"""
print(songs)
print(artists)
"""



#idVideo = playlistitems['items'][0]['snippet']['resourceId']['videoId']


url = "https://www.youtube.com/watch?v=mH0_XpSHkZo" 
video = youtube_dl.YoutubeDL({}).extract_info(url, download=False, extra_info={})

song = video["track"]
artist = video["artist"]

print(song)
print(artist)




"""
song = video["track"]
artist = video["artist"]

print(song)
print(artist)
"""
"""
for items in playlistList['items']:
    print(items)
    print()

for items in playlistList['items']:
    print(items['snippet']['title'])
    print()

"""

