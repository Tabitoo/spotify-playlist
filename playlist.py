import requests
from spotify_client import SpotifyClient
from codigo import SPOTIFY_CLIENT_ID
from codigo import SPOTIFY_SECRET_KEY
from codigo import YOUTUBE_DEVELOPER_KEY
from spotify_client.config import Config
from googleapiclient.discovery import build
import json
import youtube_dl



"""SPOTIFY"""

#configuracion y conexion 

Config.configure(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_KEY)
client = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_KEY, identifier='test-spotify-client')


#Crear playlist

def createPlaylist(token, user_id, playlist_name):
    """
    Token = Recibe el auth_code el cual es el token de spotify del usuario -> string
    User_id = recibe el el nombre de usuario de la cuenta de spotify -> string
    Playlist_name = El nombre de la platlist -> string

    """

    try:
        return client.create_playlist(token, user_id, playlist_name)
         
    except:
         print("Error al crear Playlist")



#Add the songs 

def playlist_songs(token, playlist_id, songs):

    """"
    Token = Recibe el auth_code el cual es el token de spotify del usuario -> string
    Playlist_id = Recibe el URI de la playlist -> string
    Song = recibe una lista con las canciones que queremos agregar -> list

    """

    try:
        client.add_songs_to_playlist(token,playlist_id,songs) 
    except:
        return print("Error al agregar las canciones")

    


#Conseguir access token y refresh token

def accessTokens(code,url):

    """
    code = codigo de autorizacion para conseguir el access token -> string
    url = url en donde va a ser redirigido el usuario una vez nos de permiso -> string
    
    """

    try:
        return client.get_access_and_refresh_tokens(code,url)
    except:
        return print("Error al obtener acceso")





def refreshToken(refreshToken):
    
    """
    refreshToken = recibe el refresh Token dado en la funcion accessTokens para generar un nuevo token -> string
    """

    try:
        return client.refresh_access_token(refreshToken)
    except:
        print("Error al pedir el refresh token")


def search(trackInfo,token):

    """
    trackInfo = recibe el nombre de la cancion y el artista, en un diccionario
    Token = Recibe el auth_code el cual es el token de spotify del usuario -> string

    
    """
    
    songs = []
    for track in trackInfo:
      
        query = "https://api.spotify.com/v1/search?q=track:{}%20NOT%20FuisteTu%20artist:{}&type=track&limit=1&offset=0&market=AR".format(track['track'],track['artist'])

        response = requests.get(query, headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token
                
            })

        responseJSON =  response.json()
       
        for song in responseJSON["tracks"]["items"]:
            songs.append(song['uri'])

    return songs 
        


"""YOUTUBE"""

#configuracion y conexion 

youtube = build('youtube', 'v3', developerKey=YOUTUBE_DEVELOPER_KEY)

# Consigue todas las playlist del ususario 

def getUserPlaylist(channelid):

    """
    channelId = id del canal del usuario -> string

    """
    playlists = []
    request  = youtube.playlists().list(
    part='contentDetails, snippet', 
    channelId=channelid
    )

    playlistList = request.execute()

    for nombres in playlistList['items']:
        dataPlaylist = {}
        dataPlaylist["playlist_name"] = nombres['snippet']['title']
        dataPlaylist["playlist_id"] = nombres['id']
        playlists.append(dataPlaylist)
    return playlists

# Selecciona la playlisy a elegir por el usuario

def selectPlaylist(userPlaylists, playlist):

    """

    userPlaylists = lista con todas las playlists en el canal de youtube del usuario -> List
    playlist = nombre de una playlist especifica elegida por el usuario -> string

    """

    for nombres in userPlaylists:
        if nombres['playlist_name'] == playlist:                     
            return(nombres['playlist_id'])
            break
    else:
        print('no se encontro esa playlist')

# Consigue las canciones de la playlist

def getPlaylistSongs(idPlaylist):
    """
    idPlaylist = Id de la playlist la cual queremos sacar las canciones -> String

    """

    list = []
    songsName = []

    request  = youtube.playlistItems().list(
    part='snippet, id',
    playlistId=idPlaylist,
    maxResults= 100,
    )

    playlistitems = request.execute()

    for items in playlistitems['items']:
        list.append(items['snippet']['resourceId']['videoId'])
    
    
    for videoId in list:
        videoInfo = {}
        video = youtube_dl.YoutubeDL({}).extract_info("https://www.youtube.com/watch?v=" + videoId, download=False, extra_info={})
        videoInfo['track'] = video['track']
        videoInfo['artist'] = video['artist']
        songsName.append(videoInfo)
    
    return songsName

"""Copyright Lautaro Valdez 2020-2021"""