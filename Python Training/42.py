# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included 


def func():
    tup  = ()
    tup = list(tup)
    for i in range(1,21):

        tup.append(i*i) 
    tup = tuple(tup)
    print(tup)
func()