# we can work with dates and times using the datetime library
from datetime import datetime # there is a 'datetime' feature in teh 'datetime' library
# we may also import from our own modules
from assets.utility import makeint



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
    # when using modules, we invoke strftime
    # if we used immediate-mode python, we could use strptime
    print( datetime.strftime(r, "%Y %d-%m") ) # here we provide a datetime picture

# what does Python call this module when it runs?
print(f'Python has assigned the name {__name__} to this module')

if __name__ == '__main__':
    # we can safely use the imported functions within this module
    n = 8.99
    print(makeint(n)) # 8
