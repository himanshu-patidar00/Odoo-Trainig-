# Use a list comprehension to square each odd number in a list. The list is input by a sequence of  comma-separated numbers.

l = [1,2,3,4,5,6,7,8,9]
lis = [i**2 for i in l if i%2!=0]
print(lis) 
