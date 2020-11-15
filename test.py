from spotify_client import SpotifyClient
from spotify_client.config import Config
from codigo import SPOTIFY_CLIENT_ID 
from codigo import SPOTIFY_SECRET_KEY
from codigo import CODE
from codigo import URL
import playlist
import requests
import youtube_dl
import youtube_dl.utils
codigo = "AQCVZ3qwOZD99ne0Drj_Q1zaT4X0K3fErEcQapVzmWAIi8wBzwxVHd_WOdB_Zv8meeQ6GyafHRp2XRdUJMl2UE-4bIGHljHH461PWhNyXi3lJpR1Fr__RtY-ZrEg_JUl16Sh4GhoJNwfl3XeUcEK7ZmAzLv9N4XWYZx1sDk-S5XVozMQ4IYlUJDRg1w3My5m8rI"



youtube_dl.utils.std_headers['User-Agent'] = 'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)'

url = "https://www.youtube.com/watch?v=2FCo7OxVoeY"
#video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(url, download=False)


#song = video["track"]
#artist = video["artist"]
#tag = video["tags"]


# set a custom agent (use facebook's web crawler)
#youtube_dl.utils.std_headers['User-Agent'] = "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"

# youtube_dl will now work as normal to collect 
# the song name & artist name
video = youtube_dl.YoutubeDL({}).extract_info(                            
   url, download=False)
song_name = video["track"]
artist = video["artist"]







tokenS = playlist.accessTokens(codigo,'https://www.google.com')





coso = playlist.busqueda(video['title'],video['uploader'],tokenS['access_token'])

print(coso)

"""
while True:

    name = input("Ingrese su nombre de usuario de spotify: ")
    playlistName = input("Elija un nombre para la playlist: ")
    playlist.createPlaylist(tokenS['access_token'],name,playlistName)
    datos = playlist.busqueda(q,dataType)
    print(datos)
    tokenS['access_token'] = playlist.refreshToken(tokenS['refresh_token'])
"""