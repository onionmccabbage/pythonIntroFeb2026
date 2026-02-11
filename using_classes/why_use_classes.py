# Why would we write a class??

# We can easily store data in Python objects
age = 43
fn  = 'Floella'
obe = True

flo = (43, 'Floella', True)

flod = {'age':43, 'fn':'Floella', 'obe':True}

# None of the above can validate the data members
# We cannot guarantee they are the right data type, the right shape
# Neither can we enforce facets, like min/max etc.
# Also we cannot combine any functionality here

# We would coose to use a class when we need to:
# - associate data members as a single entity
# - provide validation and limits on the data values
# - include functionality to work with the data points
