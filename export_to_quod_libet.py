# !/usr/bin/env python2
import os
import cPickle
import pickle

with open(os.path.expanduser('ratings'), 'rb') as f:
    itunes_dict = pickle.load(f)

with open(os.path.expanduser('~/.quodlibet/songs'), 'rb') as f:
    songs = cPickle.load(f)

for song in songs:
    try:
        key = song("artist") + song("album") + song("title")
        itunes_rating = itunes_dict.get(key)
        if itunes_rating:
            quodlibet_rating = itunes_rating / 100.0
            song["~#rating"] = quodlibet_rating
            print key, quodlibet_rating
    except Exception as e:
        print e

with open(os.path.expanduser('~/.quodlibet/songs'), 'wb') as f:
    songs = cPickle.dump(songs, f)
