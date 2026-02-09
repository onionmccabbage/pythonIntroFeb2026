# this module contains some useful utility code

def makeint(n):
    '''convert n to an integer, or else return default value 1'''
    if type(n) in (int, float):
        # we know we are dealing with a number
        return int(n)
    else:
        return 1
    
def stripStr(s):
    '''strip any whitespace from a string'''
    result = s.strip() # .strip() will remove any leading or trailing whitespace
    return result

# what does Python call this module when it runs?
print(f'Python has assigned the name {__name__} to this module')

if __name__ == '__main__':
    # the following code will NOT be executed if we import this module elsewhere
    # exercise this code
    values = (3, 42, 5.77, 'oops')
    for i in values:
        print(makeint(i)) 

    texts = ('   hello   ', "\n\nwow", '''\t\t   done   \t''')
    for i in texts:
        print( f'---{ stripStr(i) }---' ) # ...so we can check there is no whitespace left