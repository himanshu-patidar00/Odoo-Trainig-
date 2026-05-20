# Write a program that accepts a sequence of whitespace separated words as input and prints the words 
# after removing all duplicate words and sorting them alphanumerically.



n = input("Enter values with whitespace to seperated words := =").lower().split(" ") 
n = list(set(n))
n.sort() 
n = " ".join(n)
print(n)  