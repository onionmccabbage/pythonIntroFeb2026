# we structure Python modules using syntax
# indentation: every code block must be indented
a = 5

# single equals SETS equality, double equals CHECKS equality
if a==5:
    # this block of code MUST be indented
    print('the value is five')
elif a < 10: # > <= >= != ==
    print('the value is less than ten') # as soon as a condition matches, no other condition will be checked
else:
    print('not less than ten')

# we use indented blocks for loops
b = (5,7,3,9,2,100,-6,0)
for i in b: # we often use 'i' for iterator
    # check each value
    if i<6:
        print(f'{i} is less than 6') # f'' lets us format the string
    elif i>6:
        print(f'{i} is greater than six')
    else:
        print(i)
# any code block will end when we no longer indent
# we may declare re-useable code blocks as functions
def checkNum(x): # we may choose to pass in arguments to the function
    if type(x)==int:
        return f'The value {x} is an integer'  # we may return anything from a function (or nothing)
    elif type(x)==float:
        return f'The value {x} is a float'
    else:
        return '{x} is not a numeric value'

# we may call afunction at any time
print( checkNum() ) # NB the () are where we call the fuction
