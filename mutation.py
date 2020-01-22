import numpy as np


def mutation(value, chain_len, mutation_perc = 0.2):
    """

    :param value: must be an array of numbers to be mutated (single chromosome)
    :param chain_len
    :param mutation_perc
    :return: mutated chromosome, array
    """

    for x, index in zip(np.random.random(chain_len), range(chain_len)):
        if x < mutation_perc:
            value[index] = int(not value[index])
