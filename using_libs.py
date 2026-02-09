# we can work with dates and times using the datetime library
from datetime import datetime # there is a 'datetime' feature in teh 'datetime' library

def showToday():
    '''return a nicely formatted date'''
    now = datetime.date( datetime.today() )
    return now

def showRawDate():
    '''return the date object for today'''
    return datetime.today()

if __name__ == '__main__':
    '''exercise the code within this module'''
    n = showToday()
    print( f'Today is {n}' )
    r = showRawDate()
    print( r, type(r) )
    print( datetime.strftime(r, "%Y %d-%m") ) # here we provide a datetime picture

