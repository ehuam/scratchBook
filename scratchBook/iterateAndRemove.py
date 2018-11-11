messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]
cargo = messy_list.pop(messy_list.index(1))
messy_list.insert(0, cargo)

for i in messy_list:
    print('object', i , 'of type', type(i), 'is being evaluated')
    if type(i) == list:
        loc_list = messy_list.index(i)
        print('the location of the list is', loc_list)
        messy_list.pop(loc_list)
    elif type(i) != int:
        print(i, "of type", type(i), 'is being removed')
        messy_list.remove(i)

print(messy_list)