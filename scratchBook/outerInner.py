""" simple program to highlight nested functions"""


def main():
    pass
 
def outerInvoke():
    """Inner function nested inside of Outer./
    Inner function is fuction is invoked from outer"""
    def inner():
        print('This is inner.')
    
    print('This is outer, invoking inner.')
    inner()
    
def outerReturn():
    """ Same as outerInvoke except that inner is returned"""
    def inner():
        print('This is inner.')
    
    print('This is outer, returning inner.')
    return inner # without parenthesis the function is returned

if __name__ == "__main__":
    main()