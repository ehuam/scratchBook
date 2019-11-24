def CountingMinutesI(str): 

    # code goes here
    formatted_time = str.split('-')
    print(formatted_time)
    # '''
    totalMinutes = 0
    #first time less second time
    for time in formatted_time:
        print(time[5:])
        if time[5:] == 'am':
            totalMinutes += ( (int(time[:2]) * 60) + int(time[3:5]) )
        else:
            totalMinutes += ( (int(time[:2])+12) * 60 + int(time[3:5]))
    print(totalMinutes)
    # '''



CountingMinutesI('12:30pm-12:00pm')