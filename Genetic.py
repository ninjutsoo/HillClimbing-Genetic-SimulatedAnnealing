import math
import random
########## Parameters ##########
    # number of random initial points
n_generators = 10000
    # we choose fittest members of generators for population
n_population = 50
    # chance for every child to be mutated (swap (x, y))
mutation_rate = 0.01
    # to show how much of the population could be parents, RANK-based
selection_percentage = 30
    # number of iterations for each generator if it doesn't stop automatically
iteration = 50
current_iteration= iteration

########## Funcions ##########
    # Calculate ackley 
def ackley(x, y):
    return -20.0 * math.exp(-0.2 * math.sqrt(0.5 * (x ** 2 + y ** 2))) - math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))) + math.exp(1) + 20

    # To sort elements based on their ackley value
def fit_sort(elements):
    fit_list = []
    for i in elements:
        fit_list.append(ackley(i[0], i[1]))
    sorted_elements = [x for _,x in sorted(zip(fit_list, elements))]
    # now we have our elements sorted based on their value (in fit_list) in sorted elements.
    return sorted_elements

    # We choose "n_populatoin" fittest as the initial population
def make_population(elements, n):
    return fit_sort(elements)[:n]

    # we choose "selection_percentage" of the population as parents, and make children from the by combination and mutation
    # RANK-base
def parent_selection(elements):
    n = len(elements) * selection_percentage // 100
    parents = make_population(population, n)
    return parents

def value(element):
    for i in element: 
        print(round(ackley(i[0], i[1]), 4), end=", ")
    print()

    # We combinate and mutate n_population children from parents selected for breeding
def combination_mutation(parents, n):
    children = []
    j = len(parents)
    while (len(children) != n):
        r1 = random.randint(0, j - 1)
        r2 = random.randint(0, j - 1)
        if (r1 != r2):
            x = parents[r1][0] + parents[r2][0] // 2
            y = parents[r1][1] + parents[r2][1] // 2
            if (random.random() < mutation_rate):
                x, y = y, x
            children.append([x, y])
    return children

    # We give each element a probability based on it's fitness, then we choose "npopulation" of them. (we don't survive a duplicate of an element)
    # RANK-based
def survival_selection(elements, n):
    mating_pool = []
    survived_elements = []
    elements = fit_sort(elements)
    j = len(elements)
    i = 0
    while (j):
        x = j * [elements[i]]
        mating_pool.extend(x)
        j = j - 1
        i = i + 1
    j = len(mating_pool)
    while (n):
        z = 0
        x = mating_pool[random.randint(0, j - 1)]
        survived_elements.append(x)
        while (x in mating_pool):
            mating_pool.remove(x)
            z = z + 1
        n = n - 1
        j = j - z
    return survived_elements

# Create "n_generators" randomly, -5 < x, y < 5
# we choose "n_population" best of them for initial populatoin.
generators = []
population = []
for i in range(n_generators):
    x = random.random() * 10 - 5
    y = random.random() * 10 - 5
    generators.append([x, y])

i = iteration
population = make_population(generators, n_population)
while (i):
    parents = parent_selection(population)
    children = combination_mutation(parents, n_population)
    population = survival_selection(population + children, n_population)
    i = i - 1
min_ = ackley(fit_sort(population)[0][0], fit_sort(population)[0][1])

print("Minimum for ackley with", n_population, "population, mutation rate of", mutation_rate, ", selection percentage of", selection_percentage, "after", iteration, "generations :", min_)
