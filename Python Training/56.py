# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
 
import re 
n = input("Enter a value := ")
result = re.findall(r"\b\d+\b",n)  
print(result)


# \b is like a wall on both sides!  