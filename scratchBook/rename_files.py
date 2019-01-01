#! /usr/bin/python3

import os
index = 1
for filename in os.listdir("."):
    if filename.startswith("."): # so that private files aren't renamed.
        pass
    else:
        os.replace(filename, (index + '_' + filename)) 
    index += 1