from spotipy_app_dev.spotipy.base.classes import Track, Artist, Album


def get_track_object(track_id):
    return Track(track_id)

def get_artist_object(artist_id):
    return Artist(artist_id)

def get_album_object(album_id):
    return Album(album_id)