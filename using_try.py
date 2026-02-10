# We can handle exceptions using try...except

def askUser():
    '''invite the user to input a number'''
    # CAREFUL! We may get an exception if the user enters a non-numeric string
    try:
        user_number = input('please enter a number: ') # NB this will always be a string
        numeric_value = int(float(user_number)) # first make the string into a float, then mke the float into an int
        return numeric_value
    except: # if an exception happens within the try block, then this except block will run
        print('something went wrong')

if __name__ == '__main__':
    n = askUser() # we can call our functions to exercise this code
    print(f'The user entered {n}')



