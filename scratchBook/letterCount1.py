#! usr/bin/env/python3

"""
have function letterCount1(str) take the str parameter and return the word
with the greatest number of repeated letters.
"""

def letterCount1(str):
    words = str.split()
    scoreTracker = {}

    for index, word in enumerate(words):
        print(index, word)
        a = enumerate(word)
        print(list(a))
        # for jindex, letter in enumerate(word):
            # print(jindex, letter)
        # for letter in word:


letterCount1("hello skeeter otto")