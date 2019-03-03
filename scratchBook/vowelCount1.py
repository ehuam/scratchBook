vowels = ['a','e','i','o','u',]

word = 'galaxy'

found = {vowel: 0 for vowel in word if vowel in vowels}

for letter in word:
    if letter in found:
        found[letter] += 1

print(found)