# Problem: it seems to skip over the first value in the array
# Solution: in the while loop, i set it to greater than or equal to

# insertion sort
array = [2, 4, 6, 5, 1, 3]
print(array)
for j in range(1, len(array)):
    print('I am in loop {}'.format(j))
    key = array[j]
    print('the value of the key is {}'.format(key))
    # insert A[j] into the sorted sequence A[1...j-1]
    i = j - 1
    print('the value of i is {} and j is {}'.format(i,j))
    while i >= 0 and array[i] > key:
        array[i+1] = array[i] 
        print('the value at position {} is being set to {}'.format(i, array[i+1]))
        i = i - 1
        print('the value of i is being set to {}'.format(i))
    array[i+1] = key
    print('the value at position {index} is being set to the key value of {keyValue}'.format(index=i+1, keyValue =key))
print(array)