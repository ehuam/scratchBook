vowels = set('a','e','i','o','u')

print("Vowel search: Enter 'stop' to break out of the loop")

while True:
        word = input("Provide your word to search for a vowel\n").lower()
        
        if word == 'stop':
                break
        
        found = {vowel: word.count(vowel) for vowel in word if vowel in vowels} 
