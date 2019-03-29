def search4vowels(string):
        """ Display any vowels found in an asked-for word. """

        vowels = set ('aeiou')
        # word =input("Provide a word to search for vowels: \n")
        return vowels.intersection(set(string))
