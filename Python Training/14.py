# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

n = input("Enter a sentence := ")
lowercount = 0 
uppercount = 0
for i in n:
    if i.isalpha():
        if i.islower():
            lowercount +=1 
        elif i.isupper():
            uppercount +=1 
    
print(f"UPPER CASE := {uppercount}")
print(f"LOWER CASE := {lowercount}") 
