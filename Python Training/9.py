# Write a program that accepts sequence of lines as input and prints the lines after making all characters in
# the sentence capitalized.
lines = []  
while True:
    line = input("Enter names ")
    if(line ==""):
        print("you entered nothing")
        break  
    lines.append(line.upper()) 

for i in lines:
    print(i)    



