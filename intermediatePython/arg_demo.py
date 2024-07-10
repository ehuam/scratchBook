#!/usr/bin/python3

import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser; demonstrating the use of the add_argument method.",
        epilog="This is where you might put example usage; like how to specify a file or a host.",
    )
    return parser.parse_args()

if __name__ == '__main__':
    get_args()
