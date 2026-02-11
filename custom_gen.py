from datetime import datetime

# Python has built-in generators
g = (i for i in range(0, 1001, 5))

# we may also declare our own custom generator
def makeDT():
    '''This custom generator will yield a date-time stamp whenever required'''
    while True: # this is an endless loop
        now = datetime.now() # retrieve the computer clock time and date
        dt_str = now.strftime('%d-%m-%y %H:%M:%S') #strftime lets us use a picture to format the string
        # to make an ordinary function behave as a generator, we use 'yield' instead of 'return'
        yield dt_str

# NB any generator will be destroyed when the module stops running

if __name__ == '__main__':
    dt = makeDT() # we need an instane of our generator
    print( type(dt) )
    t1 = dt.__next__() # grab the next item from the generator
    print( t1 )