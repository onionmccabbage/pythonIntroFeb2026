# we may write a run-loop for code which needs to execute until we say stop
import random # this is one of many libraries provided with Python

while True:
    ''' check if a random number is 5
    then break out of this endless loop'''
    r = random.randint(1,10) # a random integer between 1 and 10 inclusive
    print(r)
    if r==5:
        break # this is where we break out of the while loop