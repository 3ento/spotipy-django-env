from .constants import CLIENT_CREDENTIAL_FLOW

class Album:
    def __init__(self, album_id):
        self.album_dict = CLIENT_CREDENTIAL_FLOW.album(album_id)

        self.type = self.album_dict['album_type']
        self.artists = [Artist(el['id']) for el in self.album_dict['artists']]
        self.url = self.album_dict['external_urls']['spotify']
        self.genres = self.album_dict['genres']
        self.id = self.album_dict['id']
        self.image = self.album_dict['images'][1]['url']
        self.name = self.album_dict['name']
        self.popularity = self.album_dict['popularity']
        self.release_date = self.album_dict['release_date']

class Artist:
    def __init__(self, artist_id):
        self.artist_dict = CLIENT_CREDENTIAL_FLOW.artist(artist_id)

        self.url = self.artist_dict['external_urls']['spotify']
        self.followers = self.artist_dict['followers']['total']
        self.genres = self.artist_dict['genres']
        self.id = self.artist_dict['id']
        self.image = self.artist_dict['images'][1]['url']
        self.name = self.artist_dict['name']
        self.popularity = self.artist_dict['popularity']

class Track:
    def __init__(self, track_id):
        self.track_dict = CLIENT_CREDENTIAL_FLOW.track(track_id)

        self.album = Album(self.track_dict['album']['id'])
        self.artists = [Artist(el['id']) for el in self.track_dict['artists']]
        self.duration = int(self.track_dict['duration_ms']) / 60000
        self.explicit = self.track_dict['explicit']
        self.url = self.track_dict['external_urls']['spotify']
        self.id = self.track_dict['id']
        self.is_local = self.track_dict['is_local']
        self.name = self.track_dict['name']
        self.popularity = self.track_dict['popularity']
        self.track_number = self.track_dict['track_number']