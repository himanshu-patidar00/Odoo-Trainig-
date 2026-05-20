# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line. 

str1 = input("Enter a  string first := ")
str2 = input("Enter a string second := ")

def func(str1, str2):
    if(str1>str2):
        print("first string length is maximum")
        print(str1)
    elif(str2>str1):
        print("first string length is maximum")
        print(str2)
    else:
        print(str1)
        print(str2) 
    
func(str1,str2)  
