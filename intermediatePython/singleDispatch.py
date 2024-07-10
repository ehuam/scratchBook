#!/usr/bin/python3

from functools import singledispatch

@singledispatch
def add(a,b):
    raise NotImplementedError('Unsupported Type')

@add.register(int)
def _(a,b):
    print(f'First arguement is of type {type(a)}.')
    print(a+b)

@add.register(str)
def _(a,b):
    print(f'First arguement is of type {type(a)}.')
    print(a+b)


@add.register(list)
def _(a,b):
    print(f'First arguemenet is of type {type(a)}.')
    print(a+b)

if __name__ == '__main__':
    add(1,2)
    add('Python', 'Programming')
    add([1,2,3],[5,6,7])
    print(add.registry.keys())
    add({},1)
