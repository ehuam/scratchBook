messy_list = ["a", 2, 3, 1, False, [1, 2, 3,'a','b']]

# Your code goes below here
cargo = messy_list.pop(messy_list.index(1))
messy_list.insert(0, cargo)

counter = 0
for i in range(len(messy_list)):
    try:
        if isinstance(messy_list[i], list):
            print(messy_list[i], 'is being evaluated for being a list')
            print('found a list, its length is,', len(messy_list[i]), "it's index is ", i)
            
            for j in range(0,len(messy_list[i])):
                # print(messy_list[counter][j])
                try:
                    if isinstance(messy_list[i][j], list):
                        print(messy_list[i][j], 'is being evaluated for being a list')
                    elif isinstance(messy_list[i][counter], bool):
                        print(messy_list[i][j], "is being evaluated for being a bool")
                    elif isinstance(messy_list[i][j], int):
                        print(messy_list[i][j], "is being evalauted for being an integer")                
                    else:
                        del messy_list[i][j]
                        print(messy_list[i][j], "has been removed for not being an integer")
                except IndexError as e:
                    print(e, "index error was handled, your loop continues")
                    continue
        elif isinstance(messy_list[i], bool):
            print(messy_list[i], "is being evaluated for being a bool which is a subclass of int")
            del messy_list[i]
        elif isinstance(messy_list[i], int):
            print(messy_list[i], 'has been evaluated as being an integer')
            pass
        else:
            print(messy_list[i], 'has been removed for not being an integer')
            del messy_list[i]
    except IndexError as e:
        print(e, "index error was handled, your loop continues")
print(messy_list)