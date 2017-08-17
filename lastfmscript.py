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
    lastfm_username,
    print_track,
    split_artist_track,
    TRACK_SEPARATOR,
    unicode_track_and_timestamp)

def get_top_tracks(username, number):
    top_tracks = lastfm_network.get_user(username).get_top_tracks(period=PERIOD_7DAYS)
    for i, track in enumerate(top_tracks):
        print(track.item)
    return top_tracks

def get_artist_tracks(username, artist, title):
    if TRACK_SEPARATOR in artist:
        (artist, title) = split_artist_track(artist)
    print("Searching Last.fm library...\r",)
    try:
        tracks = lastfm_network.get_user(username).get_artist_tracks(artist=artist)
    except Exception as e:
        sys.exit("Exception: " + str(e))

    total = 0
    print("\n"),  # clear line
    if title is None:  # print all
        for track in tracks:
            print_track(track)
        total = len(tracks)
    else:  # print matching titles
        find_track = pylast.Track(artist, title, lastfm_network)
        for track in tracks:
            if str(track.track).lower() == str(find_track).lower():
                print_track(track)
                total += 1
    print("Total:", total)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Show 20 last played tracks, or all the last played "
        "tracks of an artist (and optionally track)",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'artist',  nargs='?',
        help="Artist, or 'artist - track'")
    parser.add_argument(
        'track',  nargs='?',
        help="Track")
    parser.add_argument(
        '-u', '--username',
        help="Last.fm username")
    parser.add_argument(
        '-n', '--number', default=20, type=int,
        help="Number of tracks to show (when no artist given)")
    args = parser.parse_args()

    if not args.username:
        args.username = lastfm_username

    if args.artist:
        text = args.username + " last played " + args.artist
        if args.track:
            text += " - " + args.track
        text += ":"
        print(text)

        total = get_artist_tracks(args.username, args.artist, args.track)

        if total == 0:
            # Perhaps they meant to search for a user
            args.username = args.artist
            args.artist = None

    if not args.artist:
        print(args.username + " last played:")
        try:
            get_top_tracks(args.username, args.number)
        except pylast.WSError as e:
            print("Error: " + str(e))

# End of file
