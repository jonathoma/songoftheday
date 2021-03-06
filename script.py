import sys
import spotipy
import spotipy.util as util

scope = 'user-top-read'

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print('Usage: {0} username'.format(sys.argv[0]))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.current_user_top_tracks(time_range='short_term')
    for i, item in enumerate(results['items']):
        print(item['artists'][0]['name'], '-', item['name'])

else:
    print("Can't get token for", username)
