def LetterChanges(str): 

   # intialize the string to return
    modified_str = ""
    # create the lower case alphabet.
    index_of_a = ord('a')
    abcs = []
    for i in range(0,26):
        abcs.append(chr(index_of_a + i))
    
    ABCS = []    
    # create the upper case alphabet.
    for upperCase in abcs:
        ABCS.append(upperCase.upper())
    
    # create a tupe of vowels
    vowels = ('a','e','i','o','u')
    
    # first put str into a list so that it can be iterated through
    user_string = list(str)
    
    for character in user_string:
        # replace every letter in the string with the letter following it in the alphabet
        if character in ABCS:
            if ABCS.index(character) == 26:
                modified_str += ABCS[0]
            else:
                index = ABCS.index(character)
                modified_str += ABCS[index + 1]
        elif character in abcs:
            if abcs.index(character) == 26:
                modified_str += abcs[0]
            else:
                index = abcs.index(character)
                modified_str += abcs[index+1]
        else:
            modified_str += character
    
    vowels_upper = ""
    
    for character in modified_str:
        if character.lower() in vowels:
            vowels_upper += character.upper()
        else:
            vowels_upper += character

# code goes here 
    return vowels_upper
    
# keep this function call here  
print LetterChanges(raw_input())  
















  