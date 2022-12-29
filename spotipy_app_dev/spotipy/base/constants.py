import json
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy import Spotify
from decouple import config

client_id = config('client_id')
client_secret = config('client_secret')
redirect_uri = 'http://127.0.0.1:8080/'

# Client Credentials Flow = Only endpoints that do not access user information can be accessed
authO = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret)
CLIENT_CREDENTIAL_FLOW = Spotify(client_credentials_manager=authO)


# Authorization Code Flow = This flow is suitable for long-running applications in which the user grants permission only once.
def authorization_code_flow(scope, username):
    token = SpotifyOAuth(scope=scope,
                         username=username,
                         client_id=client_id,
                         client_secret=client_secret,
                         redirect_uri=redirect_uri,)

    return Spotify(auth_manager=token)

# ====================================================================== #

scopes = {
    'MODIFY_PUBLIC_PLAYLIST': 'playlist-modify-public',
    'MODIFY_PRIVATE_PLAYLIST': 'playlist-modify-private',
}

# ====================================================================== #

# bypass Spotify's 100 track limit
def get_playlist_tracks(playlist_id):
    results = CLIENT_CREDENTIAL_FLOW.playlist_items(playlist_id, additional_types=('track', ))
    tracks = results['items']
    while results['next']:
        results = CLIENT_CREDENTIAL_FLOW.next(results)
        tracks.extend(results['items'])
    return tracks

# ====================================================================== #

# pretty print for dicts
def pretty_print(dictionary):
    print(json.dumps(dictionary, indent=4))

# ====================================================================== #

"""
Local track verification

if playlist_tracks[i]['track']['is_local'] is True:
    continue
                                                """

# ====================================================================== #

def sort_dict(dicto, descending=True):
    return dict(sorted(dicto.items(), key=lambda x: x[1][0], reverse=descending))

# ====================================================================== #
