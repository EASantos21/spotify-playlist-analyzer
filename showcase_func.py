import spotipy
import time
import os
from spotipy.oauth2 import SpotifyClientCredentials
from client_auth import *

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def Divider():
    print('====================================================================')

# Function which appends track IDs to a new list
def getTrackIDs(user, playlist_id):
    item_count = 0
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
        item_count += 1
    return ids, item_count, playlist['name']

# Gets a track's features based on track ids
def getTrackFeatures(id):
    meta = sp.track(id) # returns a JSON file
    features = sp.audio_features(id) # Returns an array of dictionaries holding track features

    # meta data
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    danceability = features[0]['danceability']
    acousticness = features[0]['acousticness']
    energy = features[0]['energy']
    valence = features[0]['valence']
    track = [name, album, artist, danceability, acousticness, energy, valence]
    return track

# Gets Playlist data and prints out everything
def printPlaylistData(user, playlist_id):
    totalDanceability = 0.0
    totalEnergy = 0.0
    totalValence = 0.0
    # Retrieving all the track IDs
    ids = getTrackIDs(user, playlist_id)

    # Appending all the tracks from ids into tracks list
    tracks = []
    for i in range(len(ids[0])):
        track = getTrackFeatures(ids[0][i])
        tracks.append(track)

    # Print out every track's features and metrics
    Divider()
    print("Playlist Name: " + ids[2] + " - " + str(ids[1]) + " tracks")
    for i in tracks:
        totalDanceability += i[3]
        totalEnergy += i[5]
        totalValence += i[6]
        print("Song: " + i[0] + 
              " - Album: " + i[1] + 
              " - Artist: " + i[2] +
              " - Acousticness: " + str(round(i[4], 2)) + 
              " - Energy: " + str(round(i[5],2)))
    avgDanceability = round(totalDanceability/ids[1], 2)
    avgEnergy = round(totalEnergy/ids[1], 2)
    avgValence = round(totalValence/ids[1], 2)
    Divider()
    print("Average Danceability: " + str(avgDanceability) + ", " + checkStat('Danceability', avgDanceability) +
          " Overall Energy: " + str(avgEnergy) + ", " + checkStat('Energy', avgEnergy) +
          " Overall Valence: " + str(avgValence) + ", " + checkStat('Valence', avgValence)) 

def checkStat(metric, value): 
    if metric == 'Danceability':
        if value < 0.7: return "It seems as though it may not play well at parties and that's okay!"
        else: return "Seems like it'll be fun at parties! Make sure to invite us when it happens!"
    if metric == "Energy":
        if value < 0.5: return "Looks like you're going for something a bit more chil and laidback, we dig it!"
        else: return "Seems like you want to go crazy until you drop dead! More power to you!"
    if metric == "Valence":
        if value < 0.5: return "Seems like this playlist is for your lower times. It's okay, you got this!"
        else: return "Seems like this playlist is for the days when you feel on top of the world! Keep going!" 
    
    