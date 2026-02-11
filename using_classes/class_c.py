# here we will inherit from one class into another class
from class_b import Person

# Python has objects for list, tuple, string etc.
class MyList(list): # we inherit everythnig fromthe 'list' object
    '''This class now has all the properties and method of the built-in 'list' type'''

# We will inherit from the Person class and add property for 'logged_in'
# we will also write a new __str__
class LoggedPerson(Person):
    def __init__(self, n, a, admin=False, logged_in=False):
        # When we inherit it is a good idea to call the __init__ method of the parent
        super().__init__(n, a, admin)
        # next we deal with properties that are specific to this class
        self.logged_in = logged_in
    @property
    def logged_in(self):
        return self.__logged_in
    @logged_in.setter
    def logged_in(self, new_l):
        if type(new_l) == bool:
            self.__logged_in = new_l
        else:
            self.__logged_in = False # a sensible default
    def __str__(self):
        return f'{self.name} is {self.age} years old. Admin: {self.admin} logged in: {self.logged_in}'

if __name__ == '__main__':
    # instances of our class
    o = LoggedPerson('Oenid', 55, False)
    # we can acccess and mutate any of the properties (using get/set methods)
    o.age += 1 # this increments by 1
    o.admin = True
    print(o)


    k = MyList()
    k.append('zero')
    k.append(True)
    k.append(88)
    k.append(3.33)
    k.append([]) # here we have an empty list inside our class instance
    k.insert(0, 'changed')
    print(k)
