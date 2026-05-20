# Please write a program to print the running time of execution of "1+1" for 100 times.

import timeit 
a = "1+1"
b = timeit.timeit(a, number = 100)
print(f"{b:.4f} Seconds ")  