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

if __name__ == '__main__':
    pass