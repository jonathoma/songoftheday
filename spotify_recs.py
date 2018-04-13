"""Get Spotify recommendations."""

# Adds tracks to a playlist

import sys
import spotipy
import spotipy.util as util


def get_potential_recs(results):
    """Get potential recs from Spotify."""
    pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        exit(1)

    scope = 'user-top-read'
    token = util.prompt_for_user_token(username, scope)

    if not token:
        print("Can't get token for", username)
        exit(1)

    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_top_tracks(time_range='short_term',
                                         limit=5)
    uris = [track['uri'] for track in results['items']]
    potential_recs = sp.recommendations(seed_tracks=uris, limit=10)
    for track in potential_recs['tracks']:
        print(track['artists'][0]['name'], '-', track['name'])
