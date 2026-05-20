# Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.



class Person:
    pass 
class Male(Person):
    def getGender(self):
        print("Male")
class Female(Person): 
    def getGender(self):
        print("Female") 

obj = Male()
obj.getGender()
obj2 = Female()
obj2.getGender()
