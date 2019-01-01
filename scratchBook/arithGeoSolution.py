def ArithGeo(arr):
    ac = []
    gc = []
    
    for i in arr[1:]: # the array is set up to start off at 1 to avoid an indexError
        print("we are at element %s." % i)
        ac.append(i - (arr[arr.index(i) - 1]))
        print("the elements in array ac are %s" % ac)

        gc.append(i / (arr[arr.index(i) - 1]))
        print('the elements in array gc are %s' % gc) 
        # as a result of dividing the 1st element by the one behind it, you get a constant each time
        
    # remove duplicates 
    # if the length of set is equal to 1 then its either arithmetic or geometric
    # else return -1    
    if len(set(ac)) == 1: 
        return "Arithmetic"
    elif len(set(gc)) == 1:
        return "Geometric"
    return -1


print(ArithGeo([2,6,18,54],))