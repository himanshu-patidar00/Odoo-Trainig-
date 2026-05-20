import re 

n = input("Enter a name := ") 

result = re.findall(r"\w+@+\w+.com",n) 
if result:
    first = re.findall(r"(\w+)@",n)
    print(first[0])
else:
    print("format of email is wrong ") 
