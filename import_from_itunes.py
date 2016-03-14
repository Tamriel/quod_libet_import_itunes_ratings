# !/usr/bin/env python3
# from pyItunes import *
import pickle

library = Library('iTunes Library.xml')
ratings_dict = {}

for _, song in library.songs.items():
    if song.rating:
        key = song.artist + song.album + song.name
        ratings_dict[key] = song.rating

with open('ratings', 'wb') as f:
    pickle.dump(ratings_dict, f, protocol=2)
