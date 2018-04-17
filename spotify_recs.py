"""Get Spotify recommendations."""

# Adds tracks to a playlist

import spotipy
import spotipy.util as util


def authenticate(username):
    """Authenticate use of Spotify API."""
    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope)
    if not token:
        print("Can't get token for", username)
        exit(1)
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    return sp


def get_potential_recs(sp):
    """Get potential recs from Spotify."""
    results = sp.current_user_top_tracks(time_range='short_term',
                                         limit=5)
    uris = [track['uri'] for track in results['items']]
    potential_recs = sp.recommendations(seed_tracks=uris, limit=10)
    recs = []
    for track in potential_recs['tracks']:
        rec = track['artists'][0]['name'] + '-' + track['name']
        recs.append(rec)
    return recs


def get_spotify_recs(username):
    """Get Spotify recs."""
    sp = authenticate(username)
    return get_potential_recs(sp)
