class RecursiveFunction:
    def __init__(self, n):
        self.n = n
        print("Recursive function initialized with n =", n)

    def run(self, n=None):
        if n is None:
            n = self.n
        if n <= 0:
            return
        print("Running recursive function with n =", n)
        self.run(n - 1)

    def __del__(self):
        print("Recursive function object destroyed")


# Create an object of the class
obj = RecursiveFunction(5)

# Call the recursive function
obj.run(7)

# Destroy the object
# del obj

# NOTE! Destruction method "__del__" will be invoked implicitly (not necessary to call it explicitly)
'''
When n is 0, the function will return and the object will be destroyed by the garbage collector. The destructor will then be called automatically.
'''
