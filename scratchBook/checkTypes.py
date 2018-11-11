messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Your code goes below here
cargo = messy_list.pop(messy_list.index(1))
messy_list.insert(0, cargo)

trash = []
for i in messy_list:
    print(type(i))
    # This is the code to loop through a list within a list. it has only been tested with one nested loop.
    if isinstance(i, bool):
        trash.append(i)
    elif isinstance(i, list):
        temp = []
        for j in i:
            if isinstance(j, bool):
                print("i am am in the second loop, i am adding", j, "to list")
                temp.append(j)
            elif not isinstance(j, int):
                print('i am in the second loop, i am adding', j, 'to list')
                temp.append(j)
            else:
                print("i am not adding", j)
                pass
        print(temp)
        # print(i)
        for k in temp:
            print("im in the second loop, the value of k is", k)
            i.remove(k)
        print(i)
        # print(temp)
    elif not isinstance(i, int):
        trash.append(i)
for l in trash:
    print("i finished going through the loop and inner loop, i am now removing", l)
    messy_list.remove(l)
# print(trash)
print(messy_list)