import copy

def AlphabetSoup(str): 
    # take the STR string parameter and return the string
    # with letters in alphabetical order
    # (i.e. helloe becomes ehllo).
    # Assume numbers and punctuation symbols will not be included in the string.
    
    # make a dictionary to have value keyword relationship.
    index_of_a = ord('a')
    abc_list = []
    
    for alphabet in range(0,26):
        abc_list.append(chr(index_of_a + alphabet))
    
    abc_dictionary = {}
    
    for letter in abc_list:
        abc_dictionary[letter] = ord(letter)-index_of_a
    
    str_list = list(str)
    working_list = copy.deepcopy(str_list)
    
    index = 0
    for letter in working_list:
        if abc_dictionary[letter] >= abc_dictionary[working_list[index]]:
            temp = working_list.pop(letter)
            working_list.append(temp)
        else:
            pass
        index += 1
    # code goes here 
    return "".join(working_list)

def raw_input():
    return input("Enter the argument")


# keep this function call here  
print(AlphabetSoup(raw_input()))
















  