import copy

def AlphabetSoup(str): 
    # take the STR string parameter and return the string
    # with letters in alphabetical order
    # (i.e. helloe becomes ehllo).
    # Assume numbers and punctuation symbols will not be included in the string.
    
    # make a dictionary to have value keyword relationship.

    # solve by taking the str and creating a dictionary than sorting based on value of the keyword.
    # keyword is the letter, value is the ord(letter)

    str_list = list(str)

    str_dictionary = {}
    for letter in str_list:
        str_dictionary[letter] = ord(letter)
    
    # sorted_list = sorted(str_dictionary.items())

    for value in str_dictionary.values():
        

    return str

def raw_input():
    return input("Enter the argument")


# keep this function call here  
print(AlphabetSoup(raw_input()))
















  