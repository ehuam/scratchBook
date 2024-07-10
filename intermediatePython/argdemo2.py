#!/usr/bin/python3

import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser; demonstrating the use of the add_argument method.",
        epilog="This is where you might put example usage; like how to specify a file or a host.",
    )

    #required argument
    parser.add_argument("-x", action="store", required=True, help="Help text for option X")

    #optional arguments
    parser.add_argument("-y", help="Help text for option Y", default=False)
    parser.add_argument("-z", help="Help text for option Z", type=int)
    print(parser.parse_args())

if __name__ == '__main__':
    get_args()
    
