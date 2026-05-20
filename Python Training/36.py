# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.

def func():
    dic = {}
    for i in range(1,21):
        dic.update({i:i*i})
    
    for i in dic.values():
        print(i,end=",") 
    
func()
 