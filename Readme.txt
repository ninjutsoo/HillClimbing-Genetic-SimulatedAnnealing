********** MohammadAmin-Roshani - 610396104 - HW3 **********

********** HillClimbing **********
    *** Parameters ***
        n_generators : number of random initial points.
        step : step for making 8 new neighbours from [x, y].
        iteration : number of iterations for each generator if it doesn't stop automatically.

    *** Functions ***
        ackley : Calculate ackley 
        min_neighbour : Will find best neighbour for x, y based on ackley, if it was better than current
                        point, we will return it's index, if not we return the point itself and "change"
                        remains False (means we got no better neighbour).

    *** Procedure ***
        1. we make "n_generators" points randomly (-5 < x, y < 5) and put in generators.
        2. we pop a point from the list and will put it's best neighbour if it is
        better than it, if not we push the point in "final_generators".
        3. we continue until there is no point left in "generators" or we have done automatically
        our iterations.

    *** Output ***
        Minimum for ackley with 500 generators, step of 0.005 and 167 / 200 iterations : 0.0019196882967165152

********** SimulatedAnnealing **********
    *** Parameters ***
        n_generators : number of random initial points.
        step : step for making 8 new neighbours from [x, y].
        iteration : number of iterations for each generator if it doesn't stop automatically.
        initial_temp : initial temperature.
        final_temp : final temperature.
        alpha : step for decreasing temperature.

    *** Functions ***
        ackley : Calculate ackley 
        min_neighbour : Will find best neighbour for x, y based on ackley, if it was better than current
                        point, we will return it's index, if not we check the "current_temp" and if we 
                        didn't reach "final_temp", we accept a worse neighbour by chance of  
                        "math.exp((min_ - ackley(i[0], i[1])) / current_temp)" and will return it's index.
                        else(we reached the final temp and have no better neighbours), we remove the point
                        and push it into final_generators.

    *** Procedure ***
        1. we make "n_generators" points randomly (-5 < x, y < 5) and put in generators.
        2. we pop a point from the list and will put it's best neighbour if it is better
        than it, if not we find another neighbour (explained in "min_neighbour" func),
        but if the "current_temp" has reached to "final_temp", we just push the point 
        in final_generators.
        3. we continue until there is no point left in "generators" or we have done automatically
        our iterations.
        4. we keep decreasing the temperature (alpha) and we stop the loop if we have no generators 
        or we've done all our iterations.
    
    *** Output ***
        Minimum for ackley with 500 generators, temperature 1e-06 / 0.0005 , alpha = 1e-06 , step of 0.005 and 500 / 500 iterations : 0.0012614167550424327

********** Genetic **********
    *** Parameters ***
        n_generators : number of random initial points.
        n_population : we choose fittest members of generators for population.
        mutation_rate : chance for every child to be mutated (swap (x, y)).
                        selection_percentage : to show how much of the population could breed. (we choose RANK-based).
        iteration : number of generations that we want to go further.

    *** Functions ***
        ackley : Calculate ackley.
        fit_sort : To sort elements based on their ackley value.
        make_population : We choose "n_populatoin" fittest as the initial population.
        parent_selection : We choose "selection_percentage" of the population as parents (based on ackley). (like make_population)
        combination_mutation : We combinate and mutate n_population children from parents selected for breeding.
        survival_selection : We give each element a probability based on it's fitness, then we choose "n_population" 
                            of them. (we don't survive a duplicate of an element). we implemented RANK-based selection using mating-pool technique.

    *** Procedure ***
        1. we make "n_generators" points randomly (-5 < x, y < 5) and put in generators.
        2. we put "n_population" fittest points in population for initial population.
        3. select parents for breeding in "parent_selection" and put them in "parents".
        4. we make "n_population" children from "parents" by combination and mutation.
        5. we choose (RANK-based) "n_population" from "population + children" using survival_selection and put them 
        in "population".
        6. we keep making "iteration" generations, then we stop.

    *** Output ***
        Minimum for ackley with 50 population, mutation rate of 0.01 , selection percentage of 30 after 50 generations : 0.314445364845664