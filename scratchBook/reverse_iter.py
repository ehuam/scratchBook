"""
takes a list and iterates it from the reverse direction
"""


class Reverse_Iter:
    def __init__(self, data):
        self.index = 0
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        # print(self.index)
        self.index += -1
        if abs(self.index) > len(self.data):
            raise StopIteration
        return self.data[self.index]
