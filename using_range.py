from random import randint

# Python has a 'range' object with is very useful
# This is designed to make your coding easy, by providing a range of values 

d = range(-50,51,5) # (start, stop-before, step)

for i in d:
    print(i)

# NB a vast range of values does not need to exist in memory
# the range object will povide them on demand (thus saving memory)
endless = range(-10**1000, 10**1000)

# we can use range to generate large quantities of related data
# this saves memory

# we can use range to make a generator for any mathematical sequence
# here we generate square numbers
squares = (i*i for i in range(0,11)) # the () create a generator
print(squares)
# we may retrieve each member of the generator like this
for _ in squares: # NB the underscore _  is often used as a label for an iterator
    print(_)

# real-world use-case
# We need to provide random temperature values
# these could be used in a test to check our code responds to temperature
rndGen = (randint(0,10) for i in range(0,10**100000))

print( rndGen.__next__() ) # this lets us grab the next available member from a generator
print( rndGen.__next__() ) 
print( rndGen.__next__() ) 
print( rndGen.__next__() ) 
print( rndGen.__next__() ) 
print( rndGen.__next__() ) 
print( rndGen.__next__() ) 
print( rndGen.__next__() ) 

# As well as generators we may implement comprehension
even_number_list = [i for i in range(-100, 101, 2)] # create a list
print( type(even_number_list) ) # we havea list
# remember: this means all the generated values now exist in memory
# this is less efficient than just using a generator
print(even_number_list)
