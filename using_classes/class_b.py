# we need to gather data about a person (or several persons)
# for this we will use a class
# This 'Person' class will store the name (non-empty string) 
# and age (a positive integer)

class Person():
    '''store name and age'''
    # to bring some rigour to our class, we may choose to restrict data members
    # this is done by declaring a list of slots that are permitted
    __slots__ = ['__name', '__age', '__admin']
    # we usually start with the __init__ method
    def __init__(self, n, a, admin=False): # we may choose to provide defaults (they must come last)
        # name-mangling: we put two underscores in front of data labels
        self.name = n # this line actually calls the setter-method for 'name'
        self.age  = a # this calls the setter for 'age'
        self.admin = admin
    # we then declare accessor and mutator methods (getter/setter)
    @property # the @ makes this line a decorator
    def name(self):
        return self.__name
    # NB if we do not write a setter, this property will be read-only
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
    @property
    def admin(self):
        return self.__admin
    @admin.setter
    def admin(self, new_admin):
        '''Ensure that admin is a boolean, default to False'''
        if type(new_admin) == bool:
            self.__admin = new_admin
        else:
            self.__admin = False
    # All objects already have a __str__ method
    # The __str__ method is used whenever we call 'print'
    def __str__(self):
        # self.name calls the getter     self.__admin directly accesses the mangled value
        return f'{self.name} is {self.age} years old. Admin: {self.__admin}'
    def __repr__(self):
        # __repr__ is used in immediate-mode Python to represent an object
        return f'{self.age} year-old {self.name}. Admin: {self.__admin}'


if __name__ == '__main__':
    flo = Person('Floella', 43, True)
    Eth = Person('Ethel', 98) # the admin will default to False
    # we may access members of our class like this
    print(flo.name, flo.age, flo.admin) # here we call the getter-methods for name and age
    # we may print a class instance
    print(flo) # this calls the __str__ method
    
    # we may try to mutate data members like this
    try:
        Eth.age = False
        print(Eth.age)
    except TypeError as te:
        print( te )
    try:
        print( flo.__name ) # this will fail - we cannot access mangled members
    except Exception as err:
        print(err)
    flo.name = 'Dame Floella' # this will fail (name is read-only)
    Eth.admin = 'daft'
    print(Eth.admin) # defaults to False

    # Problem: since everything is an object, then everything may have arbitrary properties attached
    flo.wibblyoo = 'nonsense' # we can prevent this by declaring __slots__ in our class
    flo.__age = 'daft' # this is also prevented by using __slots__
    # CAREFUL - remember .__age is an arbitrary property and is NOT RELATED to self.__age
    print(flo.wibblyoo, flo.__age, flo.age)