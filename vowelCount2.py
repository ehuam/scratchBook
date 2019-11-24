vowels = {'a','e','i','o','u'}

print("Vowel search: Enter 'stop' to break out of the loop")

while True:
        word = input("Provide your word to search for a vowel\n").lower()
        
        if word == 'stop':
                break

        # using a set and intersection to find commom letters between the sets
        found = vowels.intersection(set(word))

        # using a set comprehension 
        #  val for val in set if vowel in set of vowels
        # found = {vowel: word.count(vowel) for vowel in word if vowel in vowels} 
        print(found)
