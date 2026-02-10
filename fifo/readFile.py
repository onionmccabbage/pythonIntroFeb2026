# we may retrieve text from a file system using file access object

def readFromFile():
    '''retrieve the contents of a text file and return'''
    try:
        # we need an I/O wrapper, i.e. a File Access Object
        fin = open('my_file.txt', 'rt') # 'rt' will read text
        # print(type(fin))
        r = fin.read() # read will retrieve the entire file contents
        return r
    except Exception as err:
        print(f'Problem: {err}')
    finally:
        pass

if __name__ == '__main__':
    retrieved = readFromFile()
    print( retrieved )