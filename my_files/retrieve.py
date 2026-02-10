from util import getNum

# retrieve a specific photo
import requests

def getOnePhoto(n):
    api = 'http://jsonplaceholder.typicode.com/photos'
    response = requests.get(f'{api}/{n}')
    photo = response.json() # this converts the returned JSON to a Python structure
    return photo

if __name__ == '__main__':
    # ask the user for a number
    n = getNum()
    # then retreive just that one photo
    p = getOnePhoto(n)
    print(p)