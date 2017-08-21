#!/usr/bin/env python
"""
Show 20 last played tracks, or all the last played tracks of an artist
(and optionally track)
"""
from __future__ import print_function
import argparse
import pylast
from pylast import PERIOD_7DAYS
import sys
from mylast import (
    lastfm_network,
    lastfm_username)

def get_top_tracks(username, number):
    top_tracks = lastfm_network.get_user(username).get_top_tracks(period=PERIOD_7DAYS, limit=number)
    for i, track in enumerate(top_tracks):
        print(track.item)
    return top_tracks

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Show 20 last played tracks, or all the last played "
        "tracks of an artist (and optionally track)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter) 
    parser.add_argument(
        '-u', '--username',
        help="Last.fm username")
    parser.add_argument(
        '-n', '--number', default=20, type=int,
        help="Number of tracks to show (when no artist given)")
    args = parser.parse_args()

    if not args.username:
        args.username = lastfm_username
    
    print(args.username + " top played:")
    try:
        get_top_tracks(args.username, args.number)
    except pylast.WSError as e:
        print("Error: " + str(e))
       
# End of file

