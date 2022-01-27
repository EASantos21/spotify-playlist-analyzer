import spotipy 
import time
import urllib.parse
import os
from showcase_func import *
from spotipy.oauth2 import SpotifyClientCredentials
from client_auth import *

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if __name__ == "__main__":
    while True:
        print("WELCOME TO YOUR SPOTIFY PLAYLIST SHOWCASE!")
        Divider()
        playlist = input("Please enter your playlist link: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Retrieving Playlist Data....")
        Divider()
        url_link = playlist.split('?')
        url_link = url_link[0].split('/') # Returns ['https:', '', 'open.spotify.com', 'playlist', 'playlist_id']
        playlist_id = url_link[4]
        printPlaylistData('ethanieeeel', playlist_id)

        user_continuation = input("Press Any Key to read another playlist or 'E' to Exit, then hit Enter.")
        if user_continuation == 'e' or user_continuation == 'E': break
        os.system('cls' if os.name == 'nt' else 'clear')
