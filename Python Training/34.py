# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both  included) and the values are square of keys.

def func():
    dic = {}
    for i in range(1,4):
        dic.update({i:i*i})
    print(dic) 
    
func()