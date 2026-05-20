# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? 

heads = 35
legs = 94

for rabbit in range(heads + 1):

    chicken = heads - rabbit

    total_legs = (chicken * 2) + (rabbit * 4)

    if total_legs == legs:
        print("Rabbits =", rabbit)
        print("Chickens =", chicken)

