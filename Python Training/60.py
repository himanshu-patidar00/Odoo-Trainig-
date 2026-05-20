# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).

a = int(input("Enter a value := "))
def func(n):
    if n>0:
        return func(n-1)+100 
    elif(n==0):
        return 1 
    else:
        return "Invalid input"

print(func(a)) 