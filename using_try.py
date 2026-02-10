# We can handle exceptions using try...except

def askUser():
    '''invite the user to input a number'''
    # CAREFUL! We may get an exception if the user enters a non-numeric string
    try:
        user_number = input('please enter a number: ') # NB this will always be a string
        numeric_value = int(float(user_number)) # first make the string into a float, then mke the float into an int
        return numeric_value
    # we can choose which exceptions to handle
    # You must go from specific exceptions to more general ones
    except ValueError as ve: # if a ValueError exception happens within the try block, then this except block will run
        print(f'something went wrong: {ve}')
    except Exception as err: # we may choose to handle other excpetions here
        print(f'Unknown problem:{err}')
    finally: # this is an optional block
        # finally is a good place to tidy up if there was a problem
        print('This block will run even if there is no exception')

if __name__ == '__main__':
    n = askUser() # we can call our functions to exercise this code
    print(f'The user entered {n}')



