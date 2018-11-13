messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
cargo = messy_list.pop(messy_list.index(1))
messy_list.insert(0, cargo)

gar = []

for i in messy_list:
    if isinstance(i, bool):
        gar.append(i)
    elif isinstance(i, list):
        gar.append(i)
    elif isinstance(i, int):
        pass
    else:
        gar.append(i)

# create a new loop that will delete the objects
# create a boolean variable to keep looping in case there are dupes
cont = True
while cont:
    for j in gar:
        if j in messy_list:
            messy_list.remove(j)
        else:
            cont = False