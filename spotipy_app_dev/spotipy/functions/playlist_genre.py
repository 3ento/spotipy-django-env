from ..base.constants import CLIENT_CREDENTIAL_FLOW, get_playlist_tracks, sort_dict
import time

start_time = time.time()
spotify = CLIENT_CREDENTIAL_FLOW

def get_playlist_genres(playlist_uri):
    playlist_tracks = get_playlist_tracks(playlist_uri)
    log = []

    for i in range(len(playlist_tracks)):

        if playlist_tracks[i]['track']['is_local'] is True:
            continue

        artist_uri = playlist_tracks[i]["track"]["artists"][0]["uri"]
        artist_genres = spotify.artist(artist_uri)['genres']

        [log.append(el) for el in artist_genres]

    genre_stats = sort_dict({i: log.count(i) for i in set(log)}, descending=True)

    print(f'{spotify.playlist(playlist_uri)["name"]} genre statistics:')
    for i, p in genre_stats.items():
        print(f'{i}: {p}')

