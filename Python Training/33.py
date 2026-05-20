# Define a function that can accept an integer number as input and print the "It is an even number" if the
# number is even, otherwise print "It is an odd number".

str1  = int(input("Enter a number  := ")) 
def func(str1):
    if(str1%2==0):
        print("it is a even number")
    else:
        print("it is a odd number")
    
func(str1)