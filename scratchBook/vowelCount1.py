vowels = ['a','e','i','o','u',]

print("Vowel search: Enter 'stop' to break out of the loop")

while True:
        word = input("Provide your word to search for a vowel\n")
        
        if word.lower() == 'stop':
                break
        
        found = {vowel: word.count(vowel) for vowel in word if vowel in vowels} 

        # for letter in word:
        #         if letter in found:
        #                 found[letter] += 1

        # print(len(found))
        if len(found) == 0:
                print("I didn't find any vowels")        
        for i,j in sorted(found.items()):
                print("{0} was found {1} time(s)".format(i,j))
                
        print('-'*6)