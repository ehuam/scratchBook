#!/usr/bin/env/ python3

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


#Forgiveness is better than permission
word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# use get. (second argument is default value)

word_counts = {}
for word in document:
    previous_count = word_counts.get(word,0)
    word_counts[word] = previous_count + 1

"""
DefaultDict, is like a regular dictionary.
Except when you try to look up a key it doesn't contain,
it first adds a value for it using a zero-argument
function you provided when you created it
"""

from collections import defaultdict

word_counts = defaultdict(int)
for word in document:
    word_counts[word] += 1
