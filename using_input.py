# in Python there is only ONE version of a function, there is no overloading
# there is no concept of function overloading
# This means ALL the arguments must be provided when invoking a function
# However, may may provide default argument values
def raisePower(n=1,m=1): # we may choose to provide default values
    '''raise n to the power of m'''
    return n**m

# exercise the code
a = raisePower(3,2)
print(a) # 9
b = raisePower() # here we let the function use its default values
print(b) # 1
c = raisePower(3)
print(c) # 3