dictionary = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
     'Kenneth Love': ['Python Basics', 'Python Collections']
    }

for teacher in dictionary.items():
    print(teacher, 'is of ', type(teacher), '1st loop') # returns a tuple
    for course in teacher:
        print(course, 'is of', type(course), ' 2nd loop') # goes through the tuple index 0,...