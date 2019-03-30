def search4vowels(phrase: str) -> set():
        """ 
        Return any vowels found in a supplied phrase.
        """
        vowels = set ('aeiou')
        return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters: str) -> set:
        """
        Return a set of the 'letters' found in 'phrase
        """
        # convert the letters input to a set to do set operations
        # we don't need to assign the set object to a variable becase
        # we are more interested in using the set of letters right
        # away than in storing the set in a variable for later use
        
        return set(letters).intersection(set(phrase))