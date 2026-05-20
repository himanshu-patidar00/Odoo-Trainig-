# Define a class, which have a class parameter and have a same instance parameter.

class A:
    name = "yash"

    def __init__(self,name):
        self.name = name 

obj = A("karan") 
print(obj.name) # instance 
print(A.name) # class 









