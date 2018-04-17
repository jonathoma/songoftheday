"""Main program."""

from spotify_recs import get_spotify_recs
from lastfm_recs import get_lastfm_recs

if __name__ == '__main__':
    sp_recs = get_spotify_recs('jonathanthomas3')
    lf_recs = get_lastfm_recs()
    for rec in sp_recs:
        print(rec)
    print()
    for rec in lf_recs:
        print(rec)
