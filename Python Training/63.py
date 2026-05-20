# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

def func():
    n= int(input("Enter a number := "))
    for i in range(0,n+1):
        if(i%2==0):
            yield i 
    
obj1 = func()

for i in obj1:
    print(i)    