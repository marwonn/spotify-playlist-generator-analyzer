import requests
import json
import pandas as pd

def get_playlist_audio_features(username, token, sp):
    
    query = f'https://api.spotify.com/v1/me/top/tracks?time_range=long_term&limit=50'
    
    response = requests.get(query, 
                            headers={"Content-Type":"application/json", 
                                    "Authorization": "Bearer " + f"{token}"})

    loved_tracks = response.json()

    songs = []
    ids = []
    track_name = []
    artist_name = []
    popularity = []

    songs += loved_tracks['items']

    for i in songs:
        ids.append(i['id'])
        track_name.append(i['name'])
        artist_name.append(i["artists"][0]["name"])
        popularity.append(i["popularity"])

    index = 0
    audio_features = []
    while index < len(ids):
        for entry in ids:
            if entry is not None:
                audio_features += sp.audio_features(ids[index:index + 50])
                index += 50
            else:
                continue

    features_list = []
    for features in audio_features:
        if features is not None:
            features_list.append([features['energy'], 
                                features['liveness'], 
                                features['speechiness'],
                                features['acousticness'], 
                                features['instrumentalness'],
                                features['danceability'],
                                features['valence']])
        else:
            continue

    df = pd.DataFrame(features_list, columns=['energy', 'liveness',
                                              'speechiness',
                                              'acousticness', 'instrumentalness',
                                              'danceability',
                                              'valence'])
    return df, track_name, artist_name, popularity