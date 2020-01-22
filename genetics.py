import numpy as np
import random
import math
from chromosome import Chromosome
import selection
import mutation

class Gen:
    population_size = 1000
    select_best_perc = 0.8
    cross_percentage = 0.85
    mutation_perc = 0.2

    min = -10
    max = 10
    precision = 6
    population = []

    chain_len = None

    def calculate_chain_len(self):
        self.chain_len = math.ceil(math.log2((self.max - self.min) * (10 ** self.precision)))

    def function(self, x):
        return 2 * (x ** 2) + 5

    def generate_random_population(self):
        for i in range(self.population_size):
            chromosome = Chromosome(self.chain_len, self.function, self.min, self.max)
            self.population.append(chromosome)

    def selection(self):
        self.population.sort(key=lambda x: x.f_val)

        selected_elements_count = math.floor(self.population_size * self.select_best_perc)

        return self.population[:selected_elements_count]

    def crossover(self):
        to_cross = selection.best_selection(self.population, self.select_best_perc)
        # to_cross = selection.roulette_selection(self.population, self.population_size)

        tournament_pairs = []

        selected_elements_count = math.floor(self.select_best_perc * self.population_size)

        for x in range(0, selected_elements_count, 2):
            tournament_pairs.append((to_cross[x], to_cross[x+1]))

        # for x in range(selected_elements_count // 2):
        #     element = to_cross[0]
        #     to_cross.remove(element)
        #
        #     friend = to_cross[np.random.randint(low = 0, high=len(to_cross), size = 1)[0]]
        #
        #     to_cross.remove(friend)
        #
        #     tournament_pairs.append((element, friend))

        new_chromosomes = []
        cross_index = np.random.randint(low=0, high=self.chain_len, size=1)[0]

        for x in tournament_pairs:
            if (np.random.rand() < self.cross_percentage):
                element_1_x = x[0].allel_x
                element_2_x = x[1].allel_x

                # best = element_1_x if element_1_x < element_2_x else element_2_x

                temp = element_1_x
                element_1_x = element_1_x[:cross_index] + element_2_x[cross_index:]
                element_2_x = element_2_x[:cross_index] + temp[cross_index:]

                # mutation
                element_1_x = mutation.mutation(element_1_x, self.chain_len, self.mutation_perc)
                element_2_x = mutation.mutation(element_2_x, self.chain_len, self.mutation_perc)

                new_chromosomes.append(Chromosome(self.chain_len, self.function, self.min, self.max, element_1_x))
                new_chromosomes.append(Chromosome(self.chain_len, self.function, self.min, self.max, element_2_x))

            else:
                new_chromosomes.append(x[0])
                new_chromosomes.append(x[1])

        # self.population = new_chromosomes

        self.population = []

        for _ in range(self.population_size - len(new_chromosomes)):
            chromosome = Chromosome(self.chain_len, self.function, self.min, self.max)
            self.population.append(chromosome)

        self.population = self.population + new_chromosomes


g = Gen()
g.calculate_chain_len()
g.generate_random_population()

# print([print(t.f_val, t.allel_x_dec) for t in g.population])

for i in range(1000):
    g.crossover()

g.population.sort(key=lambda x: x.f_val)

print(g.population[0].allel_x_dec)
# print(g.population)