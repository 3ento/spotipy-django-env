from ..base.constants import CLIENT_CREDENTIAL_FLOW, get_playlist_tracks, get_track_object

# setup of the authorization needed
spotify = CLIENT_CREDENTIAL_FLOW

# !!! Tracks are being compared by name, which leads to different tracks with shared names to be considered "shared"
# !!! - ex. Instrumentals' Killer from JoJo and Songs' Killer by The Ready Set

class PlaylistComparisons:
    def __init__(self, p1_only, p2_only, shared):
        self.p1_only = p1_only
        self.p2_only = p2_only
        self.shared = shared

    @staticmethod
    def get_object(track_id):
        return get_track_object(track_id)

def get_playlist_comparison(playlist_one_uri, playlist_two_uri, mode=None):

    """
    :param playlist_one_uri: URI of playlist 1
    :param playlist_two_uri: URI of playlist 2
    :param mode: which comparison to return
    :return: nothing, it prints.
    """

    # vars
    pl1 = {el['track']['uri'] for el in get_playlist_tracks(playlist_one_uri)}
    pl2 = {el['track']['uri'] for el in get_playlist_tracks(playlist_two_uri)}

    # comparisons (sets have built-in analysis methods like diff, intersection, union etc.)
    pl1_unique = pl1.difference(pl2)
    pl2_unique = pl2.difference(pl1)
    shared = pl1.intersection(pl2)

    if mode is None:
        p1u = []
        p2u = []
        unq = []
        for el in pl1_unique:
            p1u.append(get_track_object(el))

        for el in pl2_unique:
            p2u.append(get_track_object(el))

        for el in shared:
            unq.append(get_track_object(el))

    # ===================================================================================================

    # if mode == 'pl1-uni':
    #     result.append(f'{spotify.playlist(playlist_id=playlist_one_uri, fields="name")["name"]} only: \n')
    #     for el in pl1_unique:
    #         result.append(el)
    #
    # elif mode == 'pl2-uni':
    #     result.append(f'\n{spotify.playlist(playlist_id=playlist_two_uri, fields="name")["name"]} only: \n')
    #     for el in pl2_unique:
    #         result.append(el)
    #
    # elif mode == 'shared':
    #     result.append(f'\nShared: \n')
    #     for el in shared:
    #         result.append(el)

    return PlaylistComparisons(p1u, p2u, unq)