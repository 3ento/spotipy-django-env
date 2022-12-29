from ..base.constants import authorization_code_flow, get_playlist_tracks
from ..base.dev_only import username
from ..functions import playlist_create
import random

scope = 'playlist-modify-public playlist-modify-private'
username = username
token = authorization_code_flow(scope, username)

def playlist_generate(amount, base, input_location=None):

    """
    :param amount: Number of songs to be generated
    :param base: URI of playlist to be used for generation
    :param input_location: URI of playlist for the songs to be added to (leave empty to create a playlist)
    :return:
    """

    playlist_log = get_playlist_tracks(base)
    playlist_additions = []

    if input_location is None:
        input_location = playlist_create.make_playlist()

    for i in range(amount):
        playlist_additions.append(playlist_log[random.randrange(0, len(playlist_log))]['track']['uri'])

    token.playlist_add_items(input_location, playlist_additions)
