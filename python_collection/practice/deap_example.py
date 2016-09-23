#    This file is part of DEAP.
#
#    DEAP is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of
#    the License, or (at your option) any later version.
#
#    DEAP is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with DEAP. If not, see <http://www.gnu.org/licenses/>.

import random
import sys
import copy
import math
import numpy

from deap import algorithms
from points_class import *
from deap import base
from deap import creator
from deap import tools

# allConfs = [range(4), range(10,14), range(20,24)]
# allConfs = [[1,0], [.5,.5], [0,1], [3,4], [5,6]]
# allConfs = [[.5,.5], [0,1], [3,4], [5,6], [1,2], [.25, .25], [2, 3]]
# ---- creating a generator to return the next subitem of conf
def return_conf(config):
    number = 0 
    allConfsLenght = len(config) 
    while True:
        if (number >= allConfsLenght):
            return
        
        yield config[number]
        number += 1


def evalOneMax(individual):
    return sum(individual),

def specializedEval(individual):
    return (individual[0], individual[1])

def specializedMutate(individual):
    individual[1] = int(random.gauss(16 , 5.2))
    individual[0] = int(random.gauss(16 , 5.2))
    return individual, 

def doNothing(individual):
    return individual,


# ---- redefinging the eaMulPlusLambda to have a better understanding
# ---- and control over it
def eaMuPlusLambda_redefined(population, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN):
    for i in range(NGEN):
        # ----determine the offspring and evaluate the fitness,w
        offspring = algorithms.varOr(population, toolbox, LAMBDA, CXPB, MUTPB)
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        
        # ---- evaluate fitness values for the population
        invalid_ind = [ind for ind in population if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit
        
        population = toolbox.select(offspring + population, MU) 

    return population

   


def main():
    creator.create("FitnessMax", base.Fitness, weights=(-1.0, -1.0))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    toolbox = base.Toolbox()

    # Operator registering
    toolbox.register("individual", tools.initRepeat, creator.Individual)
    # toolbox.register("population", tools.initRepeat, list, toolbox.individual )

    toolbox.register("evaluate", specializedEval)
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", specializedMutate) 
    toolbox.register("select", tools.selSPEA2)

    NGEN = 20 
    MU = 40  #number of indi for the next gen
    LAMBDA = 10 #number of children
    CXPB = 0.7
    MUTPB = 0.3
    
    # ---- generating the population
    allConfs = map(lambda x: list(x), zip(range(200), range(300,500,1)))
    population = []
    for index in range(len(allConfs)):
        myGenerator = return_conf(allConfs[index])
        population.append(toolbox.individual(lambda: next(myGenerator), len(allConfs[index])))    
    
    for el in pop:
        print type(el)
    # population = eaMuPlusLambda_redefined(population, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN)
    algorithms.eaMuPlusLambda(population, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN)
    nonDominatedSort = tools.sortNondominated(population, len(population))
    print nonDominatedSort 
    return population

# testMain = False
testMain = True
if testMain:
    main()
