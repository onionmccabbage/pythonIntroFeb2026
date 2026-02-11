# a useful data type in Python is the set
# a set is a non-ordinal mutable collection of unique values of any data type
my_set = {3, 6, 3, True, 'hello'} # the {} are used for dict and for set
my_set.add('six')
my_set.add(-44)
my_set.add(1) # what will happen here....True already evaluates to 1
my_set.pop() # here we remove a member of the set. Unpredictable, but often the numerically-first value
d = my_set.pop() 
my_set.remove('six') # must already exist as a member of the set
print(my_set, d) # NB there is no predictble order to the members of a set