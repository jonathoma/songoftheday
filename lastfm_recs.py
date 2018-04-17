#!/usr/bin/env python
# coding: utf-8

"""My last.fm."""

import os
from pylast import LastFMNetwork, PERIOD_7DAYS


def authenticate():
    """Authenticate to use LastFM API."""
    try:
        API_KEY = os.environ['LASTFM_API_KEY']
        API_SECRET = os.environ['LASTFM_API_SECRET']
        LASTFM_USERNAME = os.environ['LASTFM_USERNAME']
        LASTFM_PASSWORD_HASH = os.environ['LASTFM_PASSWORD_HASH']
        LASTFM_NETWORK = LastFMNetwork(api_key=API_KEY,
                                       api_secret=API_SECRET,
                                       username=LASTFM_USERNAME,
                                       password_hash=LASTFM_PASSWORD_HASH)
        user = LASTFM_NETWORK.get_user(LASTFM_USERNAME)
    except KeyError:
        print("Run setup.sh before trying this!")
        exit(1)
    return user


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


def get_lastfm_recs():
    """Get LastFM recs."""
    user = authenticate()
    compare_factor = 20
    top_tracks = user.get_top_tracks(period=PERIOD_7DAYS,
                                     limit=compare_factor)
    potential_recs = get_potential_recs(top_tracks)
    recs = []
    for rec in potential_recs:
        if potential_recs[rec] > 1:
            recs.append(rec.item)
    return recs
