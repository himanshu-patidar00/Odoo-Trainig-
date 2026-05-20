# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive. 

import random 
lis = [i for i in range(100,201) if i%2==0]
wins = random.sample(lis,k=5)
print(wins)  

