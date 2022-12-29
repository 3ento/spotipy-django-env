from ..base.dev_only import username
from ..base.constants import authorization_code_flow

scope = 'playlist-modify-public'
username = username

spotifyObject = authorization_code_flow(scope, username)

def add_tracks(playlist_id, tracks_list):

    """
    :param playlist_id: URI of the playlist for the songs to get added in
    :param tracks_list: List of song URIs
    :return: nothing :)
    """

    spotifyObject.playlist_add_items(playlist_id, tracks_list)
