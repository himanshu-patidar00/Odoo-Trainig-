# You are required to write a program to sort the (name, age, height) tuples by ascending order where
# name is string, age and height are numbers. The tuples are input by console.

lis= []
while(True):
    n = input("Enter first name , second age  , third height := ")
    if n.lower() =="exit":
        break  
    try: 
        name,age,height = n.split()  
        age = int(age)
        height = float(height)      
        lis.append((name,age,height))   
    except ValueError: 
        print("Invalid input")  

lis.sort()
print(lis)   