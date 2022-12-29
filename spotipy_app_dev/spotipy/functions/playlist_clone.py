import spotipy
from spotipy.oauth2 import SpotifyOAuth
import base64
import requests
from ..base.constants import client_id, client_secret, redirect_uri
from ..base.dev_only import username, user_id

scope = 'playlist-modify-public ugc-image-upload'
username = username
userid = user_id

token = SpotifyOAuth(scope=scope,
                     username=username,
                     client_id=client_id,
                     client_secret=client_secret,
                     redirect_uri=redirect_uri,)

spotifyObject = spotipy.Spotify(auth_manager=token)

def make_cloned_playlist(pl_id):

    """
    :param pl_id: URI of the playlist to be cloned (have its name, description and image cover used for a new playlist)
    :return: URI of the newly created playlist
    """

    pl_name = spotifyObject.playlist(pl_id)['name']
    desc = spotifyObject.playlist(pl_id)['description']

    spotifyObject.user_playlist_create(userid, pl_name, public=True, collaborative=False, description=desc+"⁻ᵍᵉⁿᵉʳᵃᵗᵉᵈ ᵇʸ ˢᵖᵒᵗⁱᵖʸ")

    new_playlist_id = spotifyObject.current_user_playlists()['items'][0]['id']

    # convert the cover image url to base64, because that's what playlist_upload_cover_image uses
    base64url = base64.b64encode(requests.get(
        (
            spotifyObject.playlist_cover_image(pl_id)[0]['url']
        )
    ).content)

    # requires the 'ugc-image-upload' scope
    spotifyObject.playlist_upload_cover_image(new_playlist_id, base64url)

    return new_playlist_id