# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

n = input("Enter a sentence := ")
digitcount = 0 
alphabetcount = 0 
for i in n:
    if i.isdigit():
        digitcount+=1 
    elif i.isalpha():
        alphabetcount +=1 

print(f"Letters :{digitcount}")
print(f"Digits : {alphabetcount}")

