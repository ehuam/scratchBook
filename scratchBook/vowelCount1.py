vowels = ['a','e','i','o','u',]

word = input("Enter a string you want me to check for vowels\n").lower()

found = {vowel: 0 for vowel in word if vowel in vowels}

for letter in word:
    if letter in found:
        found[letter] += 1

print('I found these vowels in your word:\n', found)