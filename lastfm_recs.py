#!/usr/bin/env python
# coding: utf-8

"""My last.fm."""

import os
from pylast import LastFMNetwork, PERIOD_7DAYS


def get_potential_recs(top_tracks):
    """Get potential recs from top tracks."""
    potential_recs = {}
    for top_track in top_tracks:
        similar_tracks = top_track.item.get_similar()
        for sim_track in similar_tracks:
            if sim_track not in potential_recs:
                potential_recs[sim_track] = 0
            potential_recs[sim_track] += 1
    return potential_recs


if __name__ == '__main__':
    try:
        API_KEY = os.environ['LASTFM_API_KEY']
        API_SECRET = os.environ['LASTFM_API_SECRET']
        lastfm_username = os.environ['LASTFM_USERNAME']
        lastfm_password_hash = os.environ['LASTFM_PASSWORD_HASH']
        lastfm_network = LastFMNetwork(api_key=API_KEY,
                                       api_secret=API_SECRET,
                                       username=lastfm_username,
                                       password_hash=lastfm_password_hash)
        user = lastfm_network.get_user(lastfm_username)
        compare_factor = 12
        top_tracks = user.get_top_tracks(period=PERIOD_7DAYS,
                                         limit=compare_factor)
        potential_recs = get_potential_recs(top_tracks)
        for rec in potential_recs:
            if potential_recs[rec] > 1:
                print(rec.item)
    except KeyError:
        print("Run setup.sh before trying this!")
        exit(1)
