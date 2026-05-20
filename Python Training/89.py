# Please write a program which count and print the numbers of each character in a string input by console. 

n = input("Enter a value := ")  
emp = []
i = 0 
while(i<len(n)):
    if(n[i]  not in  emp):
        emp.append(n[i])
        print(n[i],n.count(n[i]))
    else:
        pass

    i +=1  

