# we may write a run-loop for code which needs to execute until we say stop
import random # this is one of many libraries provided with Python

# here are some utility functions
def checkIfOdd(n):
    '''return True if the value of n is odd
    otherwise, return False'''
    div1 = n/2
    div2 = n//2
    if div1 != div2: # != means not equal
        return True # it is an odd number
    else:
        return False

def myFn():
    while True:
        ''' check if a random number is 5
        then break out of this endless loop'''
        r = random.randint(1,10) # a random integer between 1 and 10 inclusive
        isOdd = checkIfOdd(r)
        print(f'The number {r} odd:{isOdd}')
        if r==5:
            break # this is where we break out of the while loop

# the following line is VERY common syntax across Python modules
if __name__ == '__main__':
    '''The above line checks to make sure this module is being run directly
    Only then will the following code be executed'''
    myFn()