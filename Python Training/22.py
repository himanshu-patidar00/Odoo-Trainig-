# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

n = input("Enter the number : ").split()
freq = {}
for word in n:
    if word in freq:
        freq[word]  += 1  
    else:
        freq[word] =1 

sortedWords = sorted(freq) # it convert to list and sorted 

for value in sortedWords:
    print(f"{value}:{freq[value]}")