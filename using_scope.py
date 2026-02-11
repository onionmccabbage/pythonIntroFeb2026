# In Python everything we write exists either in a global scope or in a local scope

# every thing that is not inside a code block exists within the global scope of this module
g = 'this is in the global scope'
# for this reason we tend to avoid the global scope where possible

def fn(): # anything within this function is destroyed when the function ends
    global g # bring a global object so it is available within this local scope
    g = 'this is in a local scope'
    return g

if __name__ == '__main__':
    print( fn() )
    print(g)