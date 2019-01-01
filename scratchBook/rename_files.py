#! /usr/bin/python3

import os
for filename in os.listdir("."):
    if filename.startswith("cheese_"):
        os.rename(filename, filename[7:])