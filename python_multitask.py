import random

def count_pi(num_of_points: int):
    in_circle: int = 0
    for i in range(num_of_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if y**2 <= (1 - x**2):
            in_circle +=1
    return float(in_circle)/num_of_points*4

