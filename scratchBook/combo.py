#!usr/bin/python3

# Alright, this one can be tricky but I'm sure you can do it.
# Create a function named combo that takes two ordered iterables. These could be tuples, lists, strings, whatever.
# Your function should return a list of tuples. Each tuple should hold the first item in each iterable, then the second set, then the third, and so on. Assume the iterables will be the same length.
# Check the code below for an example.

# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(base, *args):
    for i in base:
        pass
        for arg in args:
            pass
            for j in arg:
                print("the value of i is {} \n \
                       the value of arg is {} \n \
                       the value of j in {}".format(i,arg,j))

combo([1, 2, 3], 'abc')