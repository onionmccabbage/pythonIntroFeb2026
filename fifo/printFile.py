# the easiest way to persist text in a file is to use print

def printToFile(s):
    '''Persist the incoming argument 's' into a text file'''
    # we need a file access object
    # here, if the file does not yet exist, Python will ask the OS to create it
    fout = open('my_file.txt', 'at') # 'at' will append text
    print(s, file=fout) # send vthe print output to our file access object

if __name__ == '__main__':
    str = 'here is some important text to be persisted'
    printToFile(str)