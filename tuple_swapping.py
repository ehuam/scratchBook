#!/usr/local/bin/python3

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def add_tuples(base, *args):
    print("first normal arg:", base)
    for arg in args:
        print("another arg through *args :", arg)

print(add(5,5,))

add_tuples(10,20,'hi', 'no')

