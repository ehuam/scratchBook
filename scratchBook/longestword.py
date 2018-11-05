# code goes here
# Create a list containing the 26 letters of the alphabet
sen = input("enter your argument")
index_of_a = ord('a')
abcs = []
for i in range(0,26):
    abcs.append(chr(index_of_a + i))

# initialize an empty string that will store all the characters in the variable sen
word = ""


# Have a loop that iterates through each letter in sen.
# forcing each letter to lower case but added the letter (in original form) to a 
# string
for letter in sen:
    if letter.lower() in abcs:
        word += letter
    # to seperate words a hastag will be used and added to the the string words
    else:
        word += '#' # the hastag is going to be used to seperate words in a second loops.

# create a list of words
words =  word.split("#")

# now in the list of words find the longest one
    
print(max(words, key = len))

# keep this function call here  
 
















