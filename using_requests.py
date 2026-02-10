# We can access data from the internet using http(s)
# For this we need the requests library
import requests # we import the entire library

def getRemoteData():
    '''retrieve a load of data about photos from a remote API'''
    # Application Programming Interface
    api = 'http://jjjjjsonplaceholder.typicode.com/photos'
    # This is the sort of thing that could go wrong
    try:
        # we will use 'get' to retrieve all the JSON text
        response = requests.get(api) # this will make a request to the URL
        # we know the data is JSON in this case
        photos = response.json() # or xml, text, html etc.
        return photos
    except Exception as err: # we should consider using specific exception types
        print(f'Connection error: {err}')

if __name__ == '__main__':
    # here we can exercise the code within this module
    p = getRemoteData() # call the function
    print(p)