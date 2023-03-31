# Python program to demonstrate private members of the parent class
class C(object):
    def __init__(self):
        self.c = 21

        '''
         d is private instance variable
        Double underscore makes an instance variable private by adding double underscores before its name.
        '''
        self.__d = 42

    def parent_function(self):
        print(self.__d)

    '''
    Double underscore makes function PRIVATE
    '''
    def __private_parent_function(self):
        print(self.__d)

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

    def child_function(self):
        C.parent_function(self)

    def __private_child_function(self):
        C.parent_function(self)

object1 = D()

# produces an error as d is private instance variable
#print(object1.d)

# No error here
object1.parent_function()

# Error here (private method)
#object1.__private_parent_function()

object1.child_function()

# Error here (private method)
#object1.__private_child_function()