# Problem: it seems to skip over the first value in the array
# Solution: in the while loop, i set it to greater than or equal to

# insertion sort
array = [2, 4, 6, 5, 1, 3]
print(array)
for j in range(1, len(array)):
    key = array[j]
    # insert A[j] into the sorted sequence A[1...j-1]
    i = j - 1
    # print('the value of the key is {}'.format(key))
    while i >= 0 and array[i] > key:
        array[i+1] = array[i] 
        i = i - 1
    array[i+1] = key
print(array)