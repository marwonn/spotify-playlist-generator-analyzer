import requests
import json

def get_seed_artist(data, token):
    
    if data["seed-artist"] != "":
        query = f'https://api.spotify.com/v1/search?query={data["seed-artist"]}&type=artist&offset=0&limit=1'
    
        response = requests.get(query, 
                                headers={"Content-Type":"application/json", 
                                        "Authorization": "Bearer " + f"{token}"})

        json_response = response.json()

        for i in json_response["artists"]["items"]:
            return (i["id"])
    else:
        return "2d0hyoQ5ynDBnkvAbJKORj" # Set seed to default: Rage against the machine