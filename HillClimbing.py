import math
import random
########## Parameters ##########
    # number of random initial points
n_generators = 500
    # step for making 8 new neighbours from [x, y]
step = 0.005
    # number of iterations for each generator if it doesn't stop automatically
iteration = 200
current_iteration= iteration

########## Funcions ##########
    # Calculate ackley 
def ackley(x, y):
    return -20.0 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.exp(1) + 20
    # Calculate ackley for neighbours of [x +- step, y +- step]
global change 
change = False
def min_neighbour(x, y):
    global change
    min_ = ackley(x, y)
    min_index = [x, y]
    min_neighbour = [[x + step, y + step], [x, y + step], [x - step, y + step], [x - step, y], [x - step, y - step], [x, y - step], [x + step, y - step], [x + step, y]]
    for i in min_neighbour:
        if (ackley(i[0], i[1]) < min_):
            min_ = ackley(i[0], i[1])
            min_index = [i[0], i[1]]
            change = True
    return min_index

# Create "n_generators" randomly, -5 < x, y < 5
# we keep updating this list
generators = []
# list of our final results for n_generators generators
final_generators = []
for i in range(n_generators):
    x = random.random() * 10 - 5
    y = random.random() * 10 - 5
    generators.append([x, y])
while ((current_iteration > 0) and (generators)):
    for i in generators:
        generators.remove(i)
        new_neighbour = min_neighbour(i[0], i[1])
        if (change):
            generators.append(min_neighbour(i[0], i[1]))
        else : 
            final_generators.append(i)
        change = False
    current_iteration= current_iteration- 1
# To calculate ackley for final_generators
final_list = []
# as a high value
min_ = ackley(5, 5)
for i in final_generators:
    if (ackley(i[0], i[1]) < min_):
        min_ = ackley(i[0], i[1])
print("Minimum for ackley with", n_generators, "generators, step of", step, "and", iteration - current_iteration, "/", iteration, "iterations :", min_)