# Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic"
# if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. 
# If the sequence doesn't follow either pattern return -1. 
# An arithmetic sequence is one where the difference between each of the numbers is consistent,
#    where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio.
# Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. 
# Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain 
#   all the same elements. 

def arithGeo(arr):

    """
    if it follows a geometric pattern
        Each term after the first is multiplied by some constant or common ratio
            example [2,6,18,54], 
                    [2,(2x3),(2x3x3), (2x3x3x3)]
                        let a = 1st term = [2]
                        let c = some constant
                        let b = 2nd term = [6]
                        a*C = b
                        C = b/c
                    the pattern is that after finding the constant, the exponent would increase
    """
    # find the constant for geometric
    k = arr[0]/arr[1]
    geometric = False
    index = 0
    print(arr)

    for exponent in range(len(arr)):
        # print('the value of exponent is' , exponent)
        print("we are in loop {numberLoop}, the value of exponent is {valExp} \
                  and index is {index}.".format(numberLoop = exponent, 
                                                valExp = exponent,
                                                index = index))
        
        if arr[index] == arr[0]*k**(exponent):
            geometric = True
        else:
            geometric = False
        index += 1

    return geometric

print(arithGeo([2, 10, 12, 8, 0]))
