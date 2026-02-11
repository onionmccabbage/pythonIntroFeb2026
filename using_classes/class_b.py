# we need to gather data about a person (or several persons)
# for this we will use a class
# This 'Person' class will store the name (non-empty string) 
# and age (a positive integer)

class Person():
    '''store name and age'''
    # we usually start with the __init__ method
    def __init__(self, n, a):
        # name-mangling: we put two underscores in front of data labels
        self.__name = n # name-mangling makes it very hard to access these data members directly
        self.__age  = a # it is nearly impossible to access these from outside the class
    # we then declare accessor and mutator methods (getter/setter)
    @property # the @ makes this line a decorator
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        ''' here we can implement validation checks'''
        if type(new_name)==str and len(new_name) >0:
            self.__name = new_name
        else:
            self.__name = 'default' # we may choose to set a sensible default value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        '''validate the age is a positive integer'''
        if type(new_age) in (int, float) and new_age >0:
            self.__age = int(new_age)
        else:
            raise TypeError('Age must be a positive number')

if __name__ == '__main__':
    flo = Person('Floella', 43)
    Eth = Person('Ethel', 98)
    # we may access members of our class like this
    print(flo.__name, flo.__age) # here we call the getter-methods for name and age
    # we may mutate data members like this
    Eth.age = False
    print(Eth.age)