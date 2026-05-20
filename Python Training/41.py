# Define a function which can generate a list where the values are square of numbers between 1 and 20(both included). Then the function needs to print all values except the first 5 elements in the list.


def func():
    lis = []
    for i in range(1,21):
        lis.append(i*i)
    print(lis[5:])

func()