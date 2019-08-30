

import sys

try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed.')
except Exception as err:
    print('Some other error occured.', str(err))
    error = sys.exc_info()
    print('using sys module:', error )

class ConnectionError(Exception):
    pass

# raise ConnectionError('Cannot connect... is it time to panic?')

try:
    raise ConnectionError('Whoops')
except ConnectionError as err:
    print('Got:', str(err))
