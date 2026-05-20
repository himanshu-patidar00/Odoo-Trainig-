# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.



class A:
    def __init__(self):
        self.strr = ""

    def getString(self):
        self.strr = input("Enter string")
    
    
    def printString(self):
        self.strr = self.strr.upper()
        print(self.strr)

obj = A()
obj.getString()
obj.printString()   