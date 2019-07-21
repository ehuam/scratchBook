""" doc string """

def main():
    """turn a word into its pig latin equivalent"""

    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p',
                  'q', 'r', 's', 't', 'v', 'x', 'z', 'w', 'y']

    vowels = 'aeiou' 

    word_to_pig = input("Enter a word to pigify")
    pigged_word = ''

    if word_to_pig[0] in consonants:
        print(pigged_word + word_to_pig[1:] + 'ay' + word_to_pig[1])

if __name__ == "__main__":
    main()
