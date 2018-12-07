# import copy

def AlphabetSoup(str): 
    # take the STR string parameter and return the string
    # with letters in alphabetical order
    # (i.e. helloe becomes ehllo).
    # Assume numbers and punctuation symbols will not be included in the string.
    
    # sort () can be used on list objects. it has two optional parameters, a boolean and a function. 
    # the boolean REVERSE is to handle descending order. the function KEY serves as the key for the sort
    # comparison. for example, (key = len) would sort based on the length of the object at that index in the list.

    # sorted() does not change the original list. instead it returns a new list.
    # 

    in_str = str
    str = ''

    temp = sorted(in_str)
    return ''.join(temp)


def raw_input():
    return input("Enter the argument")


# keep this function call here  
print(AlphabetSoup(raw_input()))
















  