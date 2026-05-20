# By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

l = [12,24,35,70,88,120,155] 
lis = [l[i] for i in range(len(l)) if i%2!=0] 
print(lis)

# i%2!=0 is used for get  getting odd indexes    
# l[i] is used to get element in l 
