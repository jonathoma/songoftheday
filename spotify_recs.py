# Adds tracks to a playlist

import sys
import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_top_tracks(time_range='short_term', limit=50)
    for item in results['items']:
        print(item['artists'][0]['name'], '-', item['name'])
    print()
else:
    print("Can't get token for", username)