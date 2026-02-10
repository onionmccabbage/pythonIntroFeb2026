# ask user for a number
def getNum():
    '''ask the user to enter a number
    If it is not a number, then return 1'''
    try:
        n = input('Please enter an integer: ')
        num = int(float(n))
        return num
    except Exception as err:
        print(f'problem: {err}')
        return 1 # we have a safe default if there is an exception

if __name__ == '__main__':
    n = getNum()