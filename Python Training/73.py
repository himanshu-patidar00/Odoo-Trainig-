# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
import random
lis = [i for i in range(100,201)]
wins = random.choices(lis,k=5)
print(wins) 
