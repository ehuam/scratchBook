def MeanMode(arr): 
    """
    Have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)).
    The array will not be empty, will only contain positive integers, and will not contain more than one mode. 
    """
    # find mode
    dictionary_of_arr = { i : 0 for i in arr}
    for letter in arr:
        if letter in dictionary_of_arr:
            dictionary_of_arr[letter] += 1
    
    print(dictionary_of_arr)
    print(arr)

MeanMode((1,2,3,4,4,4))
