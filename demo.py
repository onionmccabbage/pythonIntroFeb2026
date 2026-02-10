# ways to import
import random # this imports the entire library
from random import randint # here we import one feature from the library

# modern python allows hints
# this hinting has absolutely no effect on the way Python runs
def fn()->str: # here we are hinting tht the function should return a string
    pass # pass means do nothing!!

# use our imported library
# if we imported the enture library we must use like this
f = random.randrange(0,10)
# if we import individual features we use like this
g = randint(1,10)


# we sometimes plan our code by writing outline blocks
def check():
    pass # this does nothing - we intend to come back and fill in the details later

def doWork():
    pass

def makeLog():
    pass

def main():
    pass
















