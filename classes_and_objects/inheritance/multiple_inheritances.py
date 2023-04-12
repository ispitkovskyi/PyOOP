# Python example to show the working of multiple
# inheritance


class Base1(object):
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")

    def printStr1(self):
        print(self.str1)

class Base2(object):
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")

    def printStr2(self):
        print(self.str2)

class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1 and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)

    def printAllStrs(self):
        Base1.printStr1(self)
        Base2.printStr2(self)


ob = Derived()
ob.printStrs()
ob.printAllStrs()