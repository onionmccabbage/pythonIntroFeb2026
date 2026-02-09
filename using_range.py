# Python has a 'range' object with is very useful
# This is designed to make your coding easy, by providing a range of values 

d = range(-50,51,5) # (start, stop-before, step)

for i in d:
    print(i)

# NB a vast range of values does not need to exist in memory
# the range object will povide them on demand (thus saving memory)
endless = range(-10**1000, 10**1000)
