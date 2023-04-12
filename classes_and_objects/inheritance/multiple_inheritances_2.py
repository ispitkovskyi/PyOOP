class Mother:
    mothername = ""

    # PRIVATE class variable, having preceding __ in its name
    def __init__(self, age):
        ''' NOTE!!!: If you have not-private variable ("age" instead of "__age"), then this "age" variable
            would be shared across BOTH PARENT CLASSES - Mother and Father.
            If you'd set age="30" in class Mother, then "age" variable inside class Father also was equal to "30"
            Private variables, preceded with "__" allow to have different values for variables with same name, but
            located in different parent classes (multiple inheritance)
        '''
        self.__age = age
    def mother(self):
        print(self.mothername)

    def age(self):
        print(self.__age)

class Father:
    fathername = ""

    ''' NOTE!!!: If you have not-private variable ("age" instead of "__age"), then this "age" variable
        would be shared across BOTH PARENT CLASSES - Mother and Father.
        If you'd set age="30" in class Mother, then "age" variable inside class Father also was equal to "30"
        Private variables, preceded with "__" allow to have different values for variables with same name, but
        located in different parent classes (multiple inheritance)
    '''
    def __init__(self, age):
        # PRIVATE class variable, having preceding __ in its name
        self.__age = age

    def father(self):
        print(self.fathername)

    def age(self):
        print(self.__age)
class Son(Mother, Father):
    def __init__(self, mother, father):
        self.mothername = mother
        self.fathername = father
        # Calling constructors of MULTIPLE parent classes!
        Mother.__init__(self, "30")
        Father.__init__(self, "33")

    # Call variables defined in parent classes
    def parentsUsingParentVariables(self):
        print("Father: ", self.fathername)
        print("Mother: ", self.mothername)

    # Call functions, defined in parent classes
    def parentsUsingParentMethods(self):
        print("Father: ", end='')
        self.father()
        print("Mother: ", end='')
        self.mother()

    # Call function with same name from different parent classes
    def parentAges(self):
        print("Parents ages:")
        Mother.age(self)
        Father.age(self)


s1 = Son("SITA", "RAM")
s1.parentsUsingParentVariables()
print("##########################")
s1.parentsUsingParentMethods()
print("##########################")
s1.parentAges()