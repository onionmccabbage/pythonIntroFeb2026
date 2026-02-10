# the easiest way to persist text in a file is to use print

def printToFile(s):
    '''Persist the incoming argument 's' into a text file'''
    # we need a file access object
    # here, if the file does not yet exist, Python will ask the OS to create it
    fout = open('my_file.txt', 'at') # 'at' will append text
    # NB when we use print, a new line will always be added
    print(s, file=fout) # send vthe print output to our file access object
    # if we have no further use for our file access object, we close it
    fout.close() # this is good practice

if __name__ == '__main__':
    str = 'here is some important text to be persisted'
    printToFile(str)