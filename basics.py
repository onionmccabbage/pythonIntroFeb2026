# this is a Python module
# it contains text which will be run when we execute this module

# declre variables to contain data
a = 2   # an integer
b = 7.3 # a floating point number

print(a, b)
print(type(a), type(b)) # we can see what type of data we have

# we may carry out maths operations
d = a+b
e = b-a
# we also have * /
# % will return...
print(b%a) # this return the remainder after division (in this case to a high precision)
print(b//a) # this returns the whole number of divisors (modulo)
print(2**3) # ** will raise to the power

# we will explore the data-types within Python
# numbers, strings, tuples, lists, dictionary and set

# strings are an immutable ordinal collection of characters
# we may use single quote, double quote or triple quote for strings
g = 'here is a collection of characters'
# we may access any member of a collection by it's ordinal position
print(g[8]) # 'a'
# any time we use [] to access members of a collection, this is called 'slicing'
# we may access the characters 'collection' like this:
print( g[10:20] ) # [start:stop-before]

# another collection in Python is the tuple
# a tuple is an immutable ordinal collection of any data type
j = (4, 3, 2, 8.5, 'hello', True) # NB usually whitespace is insignificant
print(j, type(j), type(g))
# we may use slicing on a tuple
print( j[3:5] )
print( j[0:5:2] ) # [start:stop-before:step]
print( j[::-1] )  # -1 means backwards!!