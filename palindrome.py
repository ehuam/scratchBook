# Have the function Palindrome(str) take the str parameter being passed and
# return the string true if the parameter is a palindrome, 
# Palindrome = (the string is the same forward as it is backward)
# otherwise return the string false. 
# For example: "racecar" is also "racecar" backwards. Punctuation and numbers will not be part of the string. 

def palindrome(str):
    isPalindrome = False
    emptySpace = ' '
    string = str.replace(emptySpace, '')

    if string[::-1] == string:
        isPalindrome = True
    
    return isPalindrome

print(palindrome("never odd or even"))
        