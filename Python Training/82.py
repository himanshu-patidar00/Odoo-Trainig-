# By using list comprehension, please write a program to print the list after removing delete numbers whichare divisible by 5 and 7 in [12,24,35,70,88,120,155].



lis = [12,24,35,70,88,120,155]

listt = [i  for i in lis if not(i%5==0 and i%7==0)]
print(listt) 

