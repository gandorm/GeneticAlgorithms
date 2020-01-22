from functools import reduce
import numpy as np
import math


def roulette_selection(chromosomes, population_size):
    sum_cost = reduce(lambda x, chromosome: chromosome.f_val + x, chromosomes, 0)

    chromosomes_weights = np.cumsum([x.f_val / sum_cost for x in chromosomes])

    selected = []
    for _ in range(population_size):
        el = np.argmax(np.random.rand() < chromosomes_weights)

        selected.append(chromosomes[el])

    return selected


def best_selection(population, select_best_perc = .8):
    population.sort(key=lambda x: x.f_val)

    selected_elements_count = math.floor(len(population) * select_best_perc)

    return population[:selected_elements_count]
