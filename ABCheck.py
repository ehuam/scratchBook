def ABCheck(str): 
    # boolean to indicate whether 'a' and 'b' are exactly 3 spaces apart
    three_apart = False
    
    a_count = 0 # a variable to hold the count of a's in the strings.
    for letter in str: #count how many a's there are in the string
        if letter == 'a': # look for lower case a
            a_count += 1
            
    a_index = str.index('a') # holds the index of the first 'a'

    temp = str # to temporarily hold str input
    for i in range(a_count): #go thru the loop only the times there is an a
        print('the value of temp is {} and a_index is {}'.format(temp, a_index))
        if 'a' in temp: # if you find an a in the substring.[index 0 (first loop): to the end ]
            a_index = temp.index('a')
            try: 
                if temp[a_index+4] == 'b':
                    three_apart = True
            except IndexError as e:
                print(e, ' the substring is shorter than the condition being checked')
                three_apart = False
        
        # print('in the {} loop, the letter a was found at position {}'.format(i, a_index))
        temp = temp[a_index+1:]

    return three_apart

print(ABCheck("Argument goes here"))