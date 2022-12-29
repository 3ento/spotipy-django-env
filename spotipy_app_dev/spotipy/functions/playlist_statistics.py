from ..base.constants import CLIENT_CREDENTIAL_FLOW, get_playlist_tracks

spotify = CLIENT_CREDENTIAL_FLOW


def get_playlist_statistics(playlist_uri):
    """
        :param playlist_uri: URI of the base playlist
        :return: nothing, it prints.
    """

    # make a dictionary of the number of times an artist appears in a playlist
    playlist_tracks = get_playlist_tracks(spotify)
    artist_count = {}
    playlist_size = len(playlist_tracks)

    for el in playlist_tracks:
        artist_name = el['track']['artists'][0]['name']
        try:
            artist_count[artist_name] += 1
        except KeyError:
            artist_count[artist_name] = 1

    # sort the dictionary by removing the one-offs from the main dict and moving them to a separate variable
    artist_count = dict(sorted(artist_count.items(),
                        key=lambda item: item[1], reverse=True))
    artist_count = {key: [val, round(val/playlist_size*100, 2)]
                    for key, val in artist_count.items() if val > 1}

    i = [el[0] for el in list(artist_count.values())]
    count_avg = sum(i)/len(i)

    artist_count = {key: [val, round(val[0]/playlist_size*100, 2)]
                    for key, val in artist_count.items() if val[0] > int(count_avg)}

    others = sum([el[0][0] for el in artist_count.values()])

    # print results with a line of code to get the playlist name
    results = spotify.playlist(playlist_id=playlist_uri, fields="name")['name']
    print(f'{results} statistics: \n')
    for key, val in artist_count.items():
        print(f'{key}: {val[0][0]}({val[1]}%)')

    print(f'Others: {others}({round(others/playlist_size*100, 2)}%)')

    # Avg. playlist popularity
    popularity = sum([el['track']['popularity'] for el in playlist_tracks]) / \
        len([el['track']['popularity'] for el in playlist_tracks])
    print(f'\n"{results}" average track popularity: {popularity:.0f}')
