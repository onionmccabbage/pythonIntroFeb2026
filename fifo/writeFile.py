# Instead of using print we may choose to use write, giving more control

def writeTofile(c):
    '''Persist the entire content of 'c' into a text file
    We will use write, and append each entry'''
    try:
        fout = open('my_log.txt', 'a') # 'a' will append, the default is text
        fout.write(c)
        fout.close()
    except Exception as err:
        print(f'Problem: {err}')
    finally:
        # if the file access object still exists, we should tidy up here
        if fout:
            fout.close()

if __name__ == '__main__':
    content = '''Here is some content
perhaps this is an error message, or a log or the results
            of a test automation'''
    writeTofile(content)