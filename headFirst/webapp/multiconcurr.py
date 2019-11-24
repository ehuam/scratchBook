from threading import Thread
import time


def execute_slowly(*args: tuple) -> None:
    for arg in args:
        print(arg)
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S:%p", localtime)
        print('printed after {} seconds'.format(result))
        time.sleep(1)

def print_hello_three_times() -> None:
    for i in range(3):
        print('hello')

def print_hi_three_times() -> None:
    for i in range(3):
        print('hi')

def print_hello() -> None:
    for i in range(4):
        time.sleep(0.5)
        print('hello')

def print_hi() -> None:
    for i in range(4):
        time.sleep(0.7)
        print('hi')
        

# t1 = Thread(target=print_hello_three_times)
# t2 = Thread(target=print_hi_three_times)

t1 = Thread(target=print_hello)
t2 = Thread(target=print_hi)

t1.start()
t2.start()
