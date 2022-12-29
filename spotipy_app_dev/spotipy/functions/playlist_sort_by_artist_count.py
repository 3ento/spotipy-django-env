from spotipy import SpotifyException
from ..functions import playlist_clone
from ..base.constants import get_playlist_tracks, authorization_code_flow
from ..base.dev_only import username

# setup of the authorization needed
scope = 'playlist-modify-public playlist-modify-private'
username = username
spotify = authorization_code_flow(scope, username)

def make_playlist_sorted_by_artist_count(playlist_uri, start=0, end=None, descending=True):
    playlist_tracks = get_playlist_tracks(playlist_uri)  # playlist tracks

    log = {}  # dictionary to contain the artists with their corresponding occurrences and URIs (ex. {"Takayan": [3, [URI, URI, URI]]})
    playlist_size = len(playlist_tracks)  # get length of playlist

    # populate the log
    sorted_playlist_id = playlist_clone.make_cloned_playlist(playlist_uri)

    if end is None:
        end = playlist_size
    if start != 0:
        start -= 1

    for i in range(start, end):
        if playlist_tracks[i]['track']['is_local'] is True:
            continue

        uri = playlist_tracks[i]['track']['uri']
        artist_name = playlist_tracks[i]['track']['artists'][0]['name']

        try:
            log[artist_name][0] += 1
            log[artist_name][1].append(uri)
        except KeyError:
            log[artist_name] = [1, [uri]]

    for el in dict(sorted(log.items(), key=lambda item: item[1], reverse=descending)).values():
        try:
            spotify.playlist_add_items(sorted_playlist_id, el[1])
        except SpotifyException:
            continue

    return sorted_playlist_id