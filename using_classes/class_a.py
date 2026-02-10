# In Python the file name has no relation to the class name

# here is a class that does absolutely nothing
class XYZ: # the () are optional
    pass

# Every time we create an oinstance of a class, it will run the __init__ method
class ABC():
    # __init__ is a bit like constructor in other languages
    def __init__(self, n): # we MUST provide self
        print(f'another instance has been created: {n}')

if __name__ == '__main__':
    # we may create instances of any class
    x = XYZ()
    print(type(x))
    a = ABC('a')
    b = ABC('b')
    c = ABC('c')