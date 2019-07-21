""" doc string """
import sys

def main():
    """turn a word into its pig latin equivalent"""
    while True:

        vowels = 'aeiou'

        word = input("Enter a word to pigify:\t")
        if word[0] in vowels:
            pig_latin = word + 'way'
        else:
            pig_latin = word[1:] + word[0] +'ay'

        print(pig_latin)

        try_again = input("\n\nTry Again? (Press Enter else n to stop)\n")
        if try_again.lower() == 'n':
            sys.exit()

if __name__ == "__main__":
    main()
