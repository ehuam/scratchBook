def sillycase(yourString):
    """
    Sillycase will take a single string as an argument
    The first half will be changed to lowercase
    The second half will be changed to uppercase
    using operator //.

    """
    mid = len(yourString)//2

    temp = []

    for i in yourString[:mid]:
        temp.append(i.lower())
        
        # print("i am going through the loop, i am working with",
            #   i, "found at index", yourString.index(i))
    for j in yourString[mid:]:
        temp.append(j.upper())

    return "".join(temp)
    

