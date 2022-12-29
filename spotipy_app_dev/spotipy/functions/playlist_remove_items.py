from ..base.constants import authorization_code_flow, get_playlist_tracks
from ..base.dev_only import username

sp = authorization_code_flow('playlist-modify-public', username)


def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def playlist_remove_items(playlist, items1=None, items_from_playlist=None):

    items = []

    if items1 is None:
        for el in get_playlist_tracks(items_from_playlist):
            if el['track']['is_local'] is True:
                continue

            items.append(el['track']['uri'])

    for el in list(divide_chunks(items, 100)):
        sp.playlist_remove_all_occurrences_of_items(playlist, el)


