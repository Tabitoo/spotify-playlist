from spotify_client import SpotifyClient
from spotify_client.config import Config
from codigo import SPOTIFY_CLIENT_ID 
from codigo import SPOTIFY_SECRET_KEY
from codigo import URL
import playlist
import requests
import youtube_dl
import youtube_dl.utils

numero = 0

while True:
    print('Antes de iniciar, la aplicacion necesita una serie de permisos para su funcionamiento')
    idCanal = input('Porfavor ingrese el id se su canal, puede encontrarlo a traves de la siguiente pagina https://support.google.com/youtube/answer/3250431?hl=es-419: ')

    

    print('autorize a la aplicacion a traves del siguiente link, una vez que sea redirigido, copie en el url la parte que dice "code="')
    print("https://accounts.spotify.com/authorize?client_id=3292435de433462e94b8cd41f52c56d1&response_type=code&redirect_uri=https%3A%2F%2Fwww.google.com&scope=playlist-modify-public")
    codigo = input('Porfavor introduzca el codigo de autorizacion: ')

    name = input("Ingrese su nombre de usuario de spotify: ")

    playlists = playlist.getUserPlaylist(idCanal)
    tokenS = playlist.accessTokens(codigo,'https://www.google.com')


    while True:

        
        namePlaylist = input('Por favor ahora escriba el nombre de la playlist de youtube que desea usar: ')

        selectedPlaylist = playlist.selectPlaylist(playlists, namePlaylist)

        

        songNames = playlist.getPlaylistSongs(selectedPlaylist)
        
        
        
        playlistName = input("Elija un nombre para la playlist: ")
        

        
        playlistUri = playlist.createPlaylist(tokenS['access_token'],name,playlistName)
        
        canciones = playlist.search(songNames,tokenS['access_token'])

        playlist.playlist_songs(tokenS['access_token'],playlistUri,canciones)
 


        tokenS['access_token'] = playlist.refreshToken(tokenS['refresh_token'])

        numero =  input('en caso de querer finalizar la ejecucion, pulse 1, de lo contrario pulse cualquier otro numero: ')

        
        if int(numero) == 1:
            break

    #Termina la ejecucion del codigo
    break
            

        

