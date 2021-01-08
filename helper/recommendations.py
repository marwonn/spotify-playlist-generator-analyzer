import requests

def gen_recommendations(payload, token, seed):

    query = f"https://api.spotify.com/v1/recommendations?limit={payload['track-count']}&market=DE&seed_genres={payload['seed-genre']}&target_danceability={int(payload['danceability'])/10}&target_valence={int(payload['valence'])/10}&target_energy={int(payload['energy']) /10}"
    
    # additional seed settings: "Shall sound like..."
    query += f'&seed_artists={seed}' 
    
    response = requests.get(query, 
                            headers={"Content-Type":"application/json", 
                                    "Authorization": "Bearer " + f"{token}"}
                                    )
    
    json_response = response.json()

    return json_response['tracks']