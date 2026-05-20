# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
try:
    num = int(input("Enter a number := "))
except ValueError:
    print("Invalid Inputs") 
else: 
    num1 = num 
    num2 = int(str(num)*2) 
    num3 = int(str(num)*3)
    num4 = int(str(num)*4) 

    result = num1+num2+num3+num4 
    print(result) 