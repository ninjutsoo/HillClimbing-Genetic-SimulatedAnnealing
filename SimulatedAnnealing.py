import math
import random
########## Parameters ##########
    # number of random initial points
n_generators = 500
    # step for making 8 new neighbours from [x, y]
step = 0.005
    # number of iterations for each generator if it doesn't stop automatically
iteration = 500
current_iteration = iteration
    # initial temperature
initial_temp = 0.0005
    # final temperature
final_temp = 0.000001
    # step for decreasing temperature
alpha = 0.000001
global current_temp, minus1, plus9
current_temp = initial_temp

########## Funcions ##########
    # Calculate ackley 
def ackley(x, y):
    return -20.0 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.exp(1) + 20
    # Calculate ackley for neighbours of [x +- step, y +- step]
global change 
change = False
def min_neighbour(x, y):
    global change, current_temp, plus9, minus1
    min_ = ackley(x, y)
    min_index = [x, y]
    min_neighbour = [[x + step, y + step], [x, y + step], [x - step, y + step], [x - step, y], [x - step, y - step], [x, y - step], [x + step, y - step], [x + step, y]]
    for i in min_neighbour:
        if (ackley(i[0], i[1]) < min_):
            min_ = ackley(i[0], i[1])
            min_index = [i[0], i[1]]
            change = True
    if (not change):
        if (current_temp > final_temp):
            change = True
            # print(math.exp((min_ - ackley(i[0], i[1])) / current_temp))
            for i in min_neighbour:
                if (random.random() < math.exp((min_ - ackley(i[0], i[1])) / current_temp)):
                    # if ((math.exp((min_ - ackley(i[0], i[1])) / current_temp)) > 0.9):
                    #     plus9 = plus9 + 1
                    #     # print(current_iteration, "is > 0.9")
                    # if ((math.exp((min_ - ackley(i[0], i[1])) / current_temp)) < 0.1):
                    #     minus1 = minus1 + 1
                    #     # print(current_iteration, "is < 0.1")
                    min_ = ackley(i[0], i[1])
                    min_index = [i[0], i[1]]
                    return min_index
        # so if change == True, means that we reached a new neighbour or we still didn't catch final temp.
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
    # print(current_iteration)
    # plus9 = 0
    # minus1 = 0
    for i in generators:
        generators.remove(i)
        new_neighbour = min_neighbour(i[0], i[1])
        if (change):
            generators.append(min_neighbour(i[0], i[1]))
        else : 
            final_generators.append(i)
        change = False
    # print(current_iteration, "+9:", plus9, "-1:", minus1)
    current_iteration = current_iteration - 1
    if ((current_temp - alpha) > final_temp):
        current_temp = current_temp - alpha
    else:
        current_temp = final_temp
# To calculate ackley for final_generators
final_list = []
# as a high value
min_ = ackley(5, 5)
for i in final_generators:
    if (ackley(i[0], i[1]) < min_):
        min_ = ackley(i[0], i[1])
print("Minimum for ackley with", n_generators, "generators, temperature", current_temp, "/", initial_temp , ", alpha =", alpha, ", step of", step, "and", iteration - current_iteration, "/", iteration, "iterations :", min_)