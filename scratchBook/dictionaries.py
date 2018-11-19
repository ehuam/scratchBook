dictionary = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
     'Kenneth Love': ['Python Basics', 'Python Collections']
    }
# # print(len(dictionary))
#
#
# for teacher in dictionary.keys():
#     print(teacher)
#
# for teacher in dictionary.values():
#     print(teacher)
#
# for teacher in enumerate(dictionary):
#     print(teacher)

for teacher in dictionary.items():
    print(teacher, 'is of ', type(teacher), '1st loop') # returns a tuple
    for course in teacher:
        print(course, 'is of', type(course), ' 2nd loop') # goes through the tuple index 0,...