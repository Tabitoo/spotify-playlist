import requests
from spotify_client import SpotifyClient
from codigo import SPOTIFY_CLIENT_ID
from codigo import SPOTIFY_SECRET_KEY
from spotify_client.config import Config



"""Spotify"""

#configuracion y conexion 

Config.configure(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_KEY)
client = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_KEY, identifier='test-spotify-client')


#Crear playlist

def createPlaylist(token, user_id, playlist_name):
    """
    Token = Recibe el auth_code el cual es el token de spotify del usuario -
    User_id = recibe el el nombre de usuario de la cuenta de spotify -> string
    Playlist_name = El nombre de la platlist -> string

    """

    try:
        client.create_playlist(token, user_id, playlist_name)
        return print("Playlist creada")
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
        return print("Canciones agregadas correctamente")
    except:
        return print("Error al agregar las canciones")


#Conseguir access token y refresh token

auth = "AQAx2GkERp9wXm2shL2JrwR-2ZX6wG6jIE6lAdOERLVsypes3DTvG_UqiGWKVLkZ51eSGz4mkhSI9_OLIVqTaGxheC_Gm532MsEpV3DdcoMhSQI4eip9RE5gF89VR7pZbi4lAucvHNtz0UdMlJUgQd583rqMgheAjmz_iuP5IrHo5EAs-G_1PcIB-e1pAeVxxac"
redirect = 'https://www.google.com'


def accessTokens(code,url):
    try:
        return client.get_access_and_refresh_tokens(code,url)
    except:
        return print("Error al obtener acceso")





def refreshToken(newToken):
    try:
        return client.refresh_access_token(newToken)
    except:
        print("Error al pedir el")

def busqueda(track,artist,key):
    try:
        query = "https://api.spotify.com/v1/search?q=track:{}%20artist:{}&type=track&market=US".format(track,artist)

        response = requests.get(query, headers={
            "Content-Type": "application/json",
             "Authorization": "Bearer " + key
             
             })

        responseJSON =  response.json()
        song = responseJSON["tracks"]["items"]
        return song
    except:
        print("Error al realizar la busqueda")

"""
    try:
        query = "https://api.spotify.com/v1/search?q=track:{}%20artist:{}&type=track&market=US".format(track,artist)

        response = requests.get(query, headers={
            "Content-Type": "application/json",
             "Authorization": "Bearer " + key
             
             })

        responseJSON =  response.json()
        song = responseJSON["tracks"]["items"]
        return song
    except:
        print("Error al realizar la busqueda")

"""





"""Youtube"""
