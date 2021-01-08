import json 
import requests

def create_playlist(username,token, uris):
    # creates new playlist
    endpoint_url = f"https://api.spotify.com/v1/users/{username}/playlists"
    request_body = json.dumps({
            "name": "Music Generator",
            "description": "by Marc",
            "public": False # public or private setting for the generated playlist
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                            "Authorization": "Bearer " + f"{token}"})

    url = response.json()['external_urls']['spotify']

    playlist_id = response.json()['id']

    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    request_body = json.dumps({
            "uris" : uris
            })
    response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json", 
                            "Authorization":f"Bearer {token}"})

    if 200 <= response.status_code <= 299:
        return True 
    else:
        return False 