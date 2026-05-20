# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2 

import math

x = 0
y = 0

while True:
    move = input("Enter direction and steps or exit : ") 
    try:
        if move.lower() == "exit":
            break 

        direction, step = move.split()  # use of  unpacking 
        step = int(step) 
        direction = direction.lower()

        if direction == "up":
            y += step

        elif direction == "down":
            y -= step

        elif direction == "left":
            x -= step

        elif direction == "right":
            x += step
        else:
            print("Invalid direction") 
    except ValueError as e:
        print("Enter input like : up 5",e)

distance = math.sqrt(x**2 + y**2)  # distance 

print(round(distance))  