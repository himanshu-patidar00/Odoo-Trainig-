# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and
# then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in
# a comma separated sequence.

n = input("Enter a number with seperated by commas after 4 digits: ").split(",")
for i in n:
    decimal = int(i,2) 
    if(decimal%5==0):
        print(i)
    else:
        print("Not divisible by 5") 
