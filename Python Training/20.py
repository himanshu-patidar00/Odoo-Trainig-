# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

class cl:
    @staticmethod
    def generator():
        n = int(input("Enter a number "))
        for i in range(n+1):
            if(i%7==0):
                yield i 

obj = cl() 
yieldelement = obj.generator() 
for i in yieldelement:
    print(i)  