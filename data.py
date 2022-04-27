from auth import get_auth
import random
import requests

def get_data(artist_id):
    access_token = get_auth()
    headers = {
        'Authorization': 'Bearer {TOKEN}'.format(TOKEN=access_token)
    }
    
    #41MozSoPIsD1dJM0CLPjZF
    URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks'.format(id=artist_id)
    data = requests.get(URL + "?market=US", headers = headers)
    data = data.json()
    
    rand = random.randint(0, len(data['tracks']) - 1)

    artistNames = []
    for i in data["tracks"][rand]["artists"]:
        artistNames.append(i["name"])

    songName = data["tracks"][rand]["name"]

    albumImage = data["tracks"][rand]["album"]["images"][0]["url"]

    previewURL = data["tracks"][rand]["preview_url"]

    spotifyURL = data["tracks"][rand]["external_urls"]["spotify"]

    info = [songName, artistNames, albumImage, previewURL, spotifyURL]

    return info

    
if __name__ == '__main__':
    x = get_data()