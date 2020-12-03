"""Find product of the two numbers a and b where a + b = 2020
"""
from itertools import combinations
import numpy as np

numbers = [int(number.replace("\n", "")) for number in open("inputs/day1_input.txt", "r").readlines()]

combination_len = 3
possible_combinations = combinations(numbers, r=combination_len)
for combination in possible_combinations:
    if np.sum(combination) == 2020:
        print(f"Numbers found : {combination}")
        print(f"The product is : {np.prod(combination)}")
