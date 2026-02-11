# In Python the file name has no relation to the class name

# here is a class that does absolutely nothing
class XYZ: # the () are optional
    pass

# Every time we create an instance of a class, it will run the __init__ method
class ABC():
    # __init__ is a bit like constructor in other languages
    def __init__(self, n): # we MUST provide self in any class method
        print(f'another instance has been created: {n}')

if __name__ == '__main__':
    # we may create instances of any class
    x = XYZ()
    print(type(x))
    # we usually work with instances of a class
    a = ABC('a')
    b = ABC('b')
    c = ABC('c')

    # here we have three instances of integer
    s = 3
    t = 4
    w = 5
    d = list()
    e = tuple()
    f = (1,2,3)