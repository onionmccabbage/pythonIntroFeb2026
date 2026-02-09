# in Python there is only ONE version of a function, there is no overloading
# there is no concept of function overloading
# This means ALL the arguments must be provided when invoking a function
# However, may may provide default argument values
def raisePower(n=1,m=1): # we may choose to provide default values
    '''raise n to the power of m'''
    return n**m

# exercise the code
# a = raisePower(3,2)
# print(a) # 9
# b = raisePower() # here we let the function use its default values
# print(b) # 1
# c = raisePower(3)
# print(c) # 3


# We may ask the user to provide an input by typing something
g = input('Please type something: ') # the module will pause until avalue is entered
print(f'The input is {g}')
print(type(g)) # using input ALWAYS returns a string

# how to convert a string to a number
def makeNum(s):
    '''where possible, convert s to a numeric value (int or float)
    If s is NOT a numeric value, return a default of 1'''
    if s.isnumeric():
        num = int(float(s)) # convert to a float then to an int just to be safe
        return num
    else:
        return 1
    
print(makeNum(g))