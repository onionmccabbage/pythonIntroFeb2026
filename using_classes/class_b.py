# we need to gather data about a person (or several persons)
# for this we will use a class
# This 'Person' class will store the name (non-empty string) 
# and age (a positive integer)

class Person():
    '''store name and age'''
    # we usually start with the __init__ method
    def __init__(self, n, a):
        self.name = n
        self.age  = a

if __name__ == '__main__':
    flo = Person('Floella', 43)
    Eth = Person('Ethel', 98)
    # we may access members of our class like this
    print(flo.name, flo.age)