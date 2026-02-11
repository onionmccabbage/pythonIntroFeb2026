# we need to gather data about a person (or several persons)
# for this we will use a class
# This 'Person' class will store the name (non-empty string) 
# and age (a positive integer)

class Person():
    '''store name and age'''
    # we usually start with the __init__ method
    def __init__(self, n, a):
        # name-mangling: we put two underscores in front of data labels
        self.name = n # this line actually calls the setter-method for 'name'
        self.age  = a # this calls the setter for 'age'
    # we then declare accessor and mutator methods (getter/setter)
    @property # the @ makes this line a decorator
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name):
        ''' here we can implement validation checks'''
        if type(new_name)==str and len(new_name) >0:
            self.__name = new_name # name-mangling makes it very hard to access these data members directly
                                   # it is nearly impossible to access these from outside the class
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
    flo = Person('Floella', True)
    Eth = Person('Ethel', 98)
    # we may access members of our class like this
    print(flo.name, flo.age) # here we call the getter-methods for name and age
    # we may mutate data members like this
    Eth.age = False
    print(Eth.age)