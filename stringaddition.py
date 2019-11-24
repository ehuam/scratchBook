#!usr/bin/python3


def NumberAddition(str):
    sum = 0
    temp_list = [char if char.isdigit() else '-' for char in str]

    holding_stage = ''.join(temp_list)
    phrase = holding_stage.split('-')

    for char in phrase:
        if char.isdigit():
            sum += int(char)

    print("debugging:\n\
           temp_list = {}\n\
           holding_stage = {}\n\
           phrase = {}".format(temp_list, holding_stage, phrase))
    return sum


print(NumberAddition('75number50'))
