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

# a list is a mutable ordinal collection of any data type
k = [6, 3.4, False, 'coffee', 'text', 42] # NB () declares a tuple, [] declares a list (like an array in other languages)
# we may use slicing to access one or more members of any collection
print( k[3:6] )
# unlike string and tuple, a list is mutable
k[2] = True
print(k, type(k), type(k[2]))

# How to choose which data type...
# for numbers its easy, just write the number!
# also for text, just always use a string
# For list and tuple they appear very similar in purpose
# but remember, we CANNOT alter a tuple once it is created
# (a list can be changed after creation)
# The general rule is: use a tuple unless you need a list

# Another data type in Python is the dictionary
# A dictionary is a non-ordinal mutable collection of any data type
# (a bit like a hash or an object in other languages) 
# a dictionary is a collection of key:value pairs
l = {'first':'Ethel', 'last':'Skronk', 'age':42, 'admin':False}
# we may access members of a dictionary like this
print( l, type(l) )
print( l['age'], type(l['age']) )
# we CANNOT use slicing since a dict is not ordinal
# We may change (mutate) members of a dict
l['admin'] = True
# we may add new members to a dict
l['lang'] = ['Python', 'Java', 'Ada']
print(l)

# It is important to remember tuple, list and dict may contain ANY data members

# we may add new members to an existing list
k.append(a)
# we may insert a new list memer between existing members
k.insert(2, 'new')

print(k)
# we may use 'pop'
k.pop()
print(k)
