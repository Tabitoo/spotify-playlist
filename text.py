
from spotify_client import SpotifyClient
from spotify_client.config import Config
from codigo import SPOTIFY_CLIENT_ID 
from codigo import SPOTIFY_SECRET_KEY
import playlist
"""
SPOTIFY_CLIENT_ID = '3292435de433462e94b8cd41f52c56d1'
SPOTIFY_SECRET_KEY = '1ef25093520b4548aa1729ab296e17e8'
AUTH_CODE = 'BQAEPapr4EOZXXWal4veZcnLWE8HpJgThTKBLBc0JyE-ec0wY2O96ap137msZd-JyIp-__dn2JdVSLKk5JRuRExDOO7Un04PuOGqsRYK6DEkXg7RtRu_aHlLMqGaYJWtTa5OOvIU6CH2VY42crT4MR8HudUiyjAxFffKp9Z287VZEOrWgz6O5FIBqxvjz1tg7uaIqOl-Vbl2xaZnBtsWrXNgOIlkRMH2kmnPQDlhWWqI'
from spotify_client import SpotifyClient
from spotify_client.config import Config


Config.configure(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_KEY)

client = SpotifyClient(SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_KEY, identifier='test-spotify-client')
user_id = "lauta1"
playlist_name = "TEST-4"

#song_name = ['spotify:track:3CYH422oy1cZNoo0GTG1TK', 'spotify:track:4Ws314Ylb27BVsvlZOy30C']
#client.create_playlist(AUTH_CODE,user_id,playlist_name)
#Playlist_ID = "3NI721NPLpw1hgOBuxq2vX"
#client.add_songs_to_playlist(AUTH_CODE,Playlist_ID,song_name)
client.create_playlist(AUTH_CODE,user_id,playlist_name)

"""
spotifiId= SPOTIFY_CLIENT_ID
secret_code = SPOTIFY_SECRET_KEY
user_name = 'lauta1'
nombre = 'prueba3'

playlist.createPlaylist(auth,user_name,nombre)
