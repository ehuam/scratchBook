# messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
# cargo = messy_list.pop(messy_list.index(1))
# messy_list.insert(0, cargo)

# gar = []

# for i in messy_list:
#     if isinstance(i, bool):
#         gar.append(i)
#     elif isinstance(i, list):
#         gar.append(i)
#     elif isinstance(i, int):
#         pass
#     else:
#         gar.append(i)

# # create a new loop that will delete the objects
# # create a boolean variable to keep looping in case there are dupes
# cont = True
# while cont:
#     for j in gar:
#         if j in messy_list:
#             messy_list.remove(j)
#         else:
#             cont = False


class toDoList:
    def __init__(self, quantity = 0):
        self.quantity = quantity
        
        
class GroceryList(toDoList):
    def __init__(self):
        self.__items = []

    def __iter__(self):
        self.__index = -1
        return self
    
    def __next__(self):
        if self.__index >= (len(self.__items)-1):
            raise StopIteration
        self.__index += 1
        lineItem = self.__items[self.__index]
        return lineItem


    def addItems(self, item = None):
        self.__items.append(item)

    def length(self):
        return len(self.__items)

class Item:
    def __init__(self, name = ''):
        self.__name = name

    @property
    def name(self):
        return self.__name

a = Item('Apples')
b = Item('Cars')

mayGroceries = GroceryList()
mayGroceries.addItems(a)
mayGroceries.addItems(b)

print(mayGroceries.length())

for item in mayGroceries:
    print(item.name)