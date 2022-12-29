import random
from ..functions import playlist_add_songs
from ..base.constants import CLIENT_CREDENTIAL_FLOW, get_playlist_tracks

# setup of the authorization needed
spotify = CLIENT_CREDENTIAL_FLOW

def get_recommendation_log(playlist_URI, seed_size=5, seed_start=None, seed_end=None):

    """
    :param seed_end: Ending index of the songs to be taken for recommendations
    :param seed_start: Starting index of the songs to be taken for recommendations
    :param playlist_URI: URI of the playlist the recommendations are going to be based on (ex. spotify:playlist:1qqtuilSwuZacPKl5YVcPI)
    :param seed_size: the amount of songs used to generate a recommendation (between 1 and 5)
    :return: a list of recommended song URIs
    """

    playlist_tracks = get_playlist_tracks(playlist_URI)  # playlist object of the base playlist
    log = []  # list of the playlist tracks, in URIs
    recommendation_log = []  # list of recommenced songs, in URIs
    curr_seed = []  # list of current songs used for a recommendation, based on the seed_size
    seed_start = seed_start
    seed_end = seed_end

    for el in playlist_tracks:
        if el['track']['is_local'] is True:
            continue
        log.append(el['track']['uri'])

    # shuffling the order of songs to get songs to get a more mean recommendation, remove to get recommendations in line with the playlist order
    random.shuffle(log)

    if seed_end is None and seed_start is None:
        seed_end = len(log)
        seed_start = 0

    for i in range(seed_start, seed_end):
        curr_seed.append(log[i])

        if len(curr_seed) == seed_size:
            recommendation_log.append(spotify.recommendations(
                seed_genres=None,
                seed_artists=None,
                seed_tracks=curr_seed,
                limit=1)['tracks'][0]['uri'])

            curr_seed = []

    # use the last songs that didn't make it into a full list
    if len(curr_seed) > 0:
        recommendation_log.append(spotify.recommendations(
            seed_genres=None,
            seed_artists=None,
            seed_tracks=curr_seed,
            limit=1)['tracks'][0]['uri'])

    return recommendation_log

def add_recommended_songs(playlist_URI, base_playlist_URI=None, seed_size=5, seed_start=None, seed_end=None):

    """
    :param seed_end: Ending index of the songs to be taken for recommendations
    :param seed_start: Starting index of the songs to be taken for recommendations
    :param seed_size: The amount of songs used to generate a recommendation (between 1 and 5)
    :param playlist_URI: URI of the playlist for the songs to be added to
    :param base_playlist_URI: URI of the playlist to get recommendations from
    :return:
    """

    if base_playlist_URI is None:
        playlist_add_songs.add_tracks(
            playlist_URI, get_recommendation_log(
                playlist_URI,
                seed_size,
                seed_start,
                seed_end))
    else:
        playlist_add_songs.add_tracks(
            playlist_URI, get_recommendation_log(
                base_playlist_URI,
                seed_size,
                seed_start,
                seed_end))
