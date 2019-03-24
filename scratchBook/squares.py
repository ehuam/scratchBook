def squares(n):

    print("Generating squares from 1 to {0}".format(n**2))

    for i in range(1, n+1):
        yield i ** 2

gen = squares(5)

for x in gen:
    print(x,'\n', end = " ")

for x in gen:
    print('the value of x in iterator gen is '.format(x))