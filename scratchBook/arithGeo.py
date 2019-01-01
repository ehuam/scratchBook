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

    # with an arithmetic equation, we have b - a  = difference. summ of the element in arithmethic equation
    # would be the number of elments times a plus the number of elements times the difference. 
    # for an arithmetic equation of 3 elements, i.e.:
    #                                               [2,4,6,8], let a = 2, let b = 4, difference = b-a = 2
    #                                               sum of the array would be = 20 = 4(a) + 4!*difference
    difference = arr[1]-arr[0]
    # for value in range(1, len(arr)+1):
    #     print(value)
    sum = 0
    sum += (len(arr)*arr[0]) - arr[0] # so it doesn't double count arr[0] twice
    print(sum)
    
    for factorial in range(1,len(arr)):
        sum+= difference**factorial


    
    inputSum = 0
    for element in arr:
        inputSum += element

    print('value of arr is {arr},\
           value of geometric is {geometric}\
           value of local sum is {created} and input sum {input}\
           '.format(arr = arr, geometric = geometricArray, created = sum, input = inputSum))
    if geometricArray == arr:
        return 'Geometric'
    elif sum == inputSum:
        return 'Arithmetic'
    else:
        return -1
    # return geometric

print(arithGeo([2, 4, 6, 8]))
