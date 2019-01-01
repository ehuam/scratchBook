#! /usr/bin/python3

""""
code snippet to rewrite files in a directory.

current bug: if there are hidden files, the index keeps counting. 
1/1/19: fixing the bug by only incrementing the index if it's not a hidden file (a file starting with a period)
"""

import os
index = 1
for filename in os.listdir("."):
    if filename.startswith("."): # so that private files aren't renamed.
        pass
    else:
        os.replace(filename, (str(index) + '_' + filename)) 
        index += 1
    
