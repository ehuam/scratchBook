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
    if it follows a geometric pattern. Return "Geometric"
        Each term after the first is multiplied by some constant or common ratio
            example [2,6,18,54], 
                    [2,(2x3),(2x3x3), (2x3x3x3)]
                        let a = 1st term = [2]
                        let c = some constant
                        let b = 2nd term = [6]
                        a*C = b
                        C = b/c
                    the pattern is that after finding the constant, the exponent would increase

    if it follows an arithmetic pattern. Return "Arithmetic"
        one where the difference between each of the numbers is consistent
            example [2, 4, 6, 8]
                    [a+0, a+K, a+K+K, a+k+k]
    """
    # find the constant for geometric
    k = arr[1]/arr[0]
    geometricArray = []
    arithmeticArray = []
    
    # we prove arr is a geometric by assuming it follows a pattern by creating a geometric pattern using
    # arr[0] and arr[1]. geometricArray should be equal to arr if true.
    for exponent in range(len(arr)):
        geometricArray.append(int((k**exponent)*arr[0]))

    # print('value of arr is {arr},\
    #        value of geometric is {geometric}\
    #        value of arithmetic is {arithmetic}'.format(arr = arr, geometric = geometricArray, arithmetic = arithmeticArray))
    if geometricArray == arr:
        return 'Geometric'
    elif arithmeticArray == arr:
        return 'Arithmetic'
    else:
        return -1
    # return geometric

print(arithGeo([2, 4, 6, 8]))
