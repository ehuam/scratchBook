#! /usr/bin/python3

""""
code snippet to rewrite files in a directory and give them an index number starting at one.

bug: if there are hidden files, the index keeps counting. Fixed
        1/1/19: fixing the bug by only incrementing the index if it's not a hidden file (a file starting with a period)

issue: renaming files keeps prefixing, should be someway to only run once, and somehow also be able store what it was before.
        potential solution: creating a text file that has the original names.


"""

import os
index = 1
for filename in os.listdir("."):
    if filename.startswith("."): # so that private files aren't renamed.
        pass
    else:
        os.replace(filename, (str(index) + '_' + filename)) 
        index += 1
    
