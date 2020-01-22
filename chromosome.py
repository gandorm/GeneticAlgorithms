import numpy as np

class Chromosome():
    allel_x = None

    allel_x_string = None

    allel_x_dec = None
    f_val = None
    min = None
    max = None
    chain_len = 0

    def __init__(self, chain_len, cost_function, min, max, body = None):
        self.chain_len = chain_len
        self.min = min
        self.max = max
        if (body):
            self.save_chromosome(cost_function, body)
        else:
            self.generate_random_chromosome(cost_function)

    def save_chromosome(self, cost_function, body):
        self.allel_x = body
        self.allel_x_string = ''.join(([str(a) for a in self.allel_x]))
        self.allel_x_dec = self.chromosome_to_dec(self.allel_x_string)
        self.f_val = cost_function(self.allel_x_dec)

    def chromosome_to_dec(self, value):
        return self.min + int(value, 2) * ((self.max - self.min) / ((2 ** self.chain_len)- 1))

    def dec_to_bin(self, value):
        return self.min + value * ((self.max - self.min) / ((2 ** self.chain_len)- 1))

    def generate_random_chromosome(self, cost_function):
        chromosome = np.ones(self.chain_len)
        # self.allel_x_dec = np.random.randint(low = self.min, high= self.max, size = 1)[0]
        self.allel_x = [0 if np.random.rand() >= .5 else 1 for _ in chromosome]
        # self.allel_x = self.dec_to_bin(self.allel_x_dec)
        self.allel_x_string = ''.join(([str(a) for a in self.allel_x]))
        self.allel_x_dec = self.chromosome_to_dec(self.allel_x_string)
        self.f_val = cost_function(self.allel_x_dec)
