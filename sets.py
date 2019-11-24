COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(set_input):
    # input is a supplied set with one element in it which acts like a list but has unique values

    # create a variable that will hold the key_value
    key_found = []

    # compare the input with the values of each key in Courses. if there is a match between the input and the value set
    for course in COURSES:
        if set_input.intersection(COURSES[course]) != set():
            key_found.append(course)
    
    # print(key_found)
    # return the key for that
    return key_found
    
    
a = {'Python'}    

# print(covers(a))

def covers_all(single_set):
    key_found = []
    for course in COURSES:
        if single_set.difference(COURSES[course]) == set():
            key_found.append(course)

    return key_found

b = {'conditions', 'input'}

print(covers_all(b))