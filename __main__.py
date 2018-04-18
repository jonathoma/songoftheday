"""Main program."""

from spotify_recs import get_spotify_recs
from lastfm_recs import get_lastfm_recs

if __name__ == '__main__':
    print('Spotify Recs: ')
    for rec in get_spotify_recs('jonathanthomas3'):
        print(rec)
    print()
    print('LastFM Recs:')
    for rec in get_lastfm_recs():
        print(rec)
