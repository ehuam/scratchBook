def ArrayAdditionI(arr): 

    # code goes here 
    addsUp = False
    arr.sort(reverse = True)
    sum = 0
    for i in arr[1:]:
        sum += i
        if sum == arr[0]:
            addsUp = True
            break
    print('the value of sum is %s and the value of arr at index 0 is %s' % (sum, arr[0]))       
    return addsUp
    
print(ArrayAdditionI([3,5,-1,8,12]))