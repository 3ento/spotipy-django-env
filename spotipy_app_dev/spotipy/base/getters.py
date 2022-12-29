from spotipy_app_dev.spotipy.base.classes import Track


def get_track_object(track_id):
    return Track(track_id)