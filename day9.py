"""Find the first number which is not the sum of two numbers among the 25 previous.
"""
from itertools import combinations
import numpy as np

code_raw = open("inputs/day9_input.txt").readlines()
preambule_size = 25

numbers = [int(number.replace("\n", "")) for number in code_raw]

for num_id, number in enumerate(numbers[preambule_size:]):
    possible_combinations = combinations(numbers[num_id:num_id+preambule_size], r=2)
    number_is_valid = False
    for combination in possible_combinations:
        if np.sum(combination) == number:
            number_is_valid = True
    if not number_is_valid:
        print(f"First invalid number in code is : {number}")
        contiguous_range_size = 2
        while True:
            range_found = False
            contiguous_range = None
            for num_id, numb in enumerate(numbers[0:-contiguous_range_size]):
                contiguous_range = numbers[num_id:num_id+contiguous_range_size]
                if np.sum(contiguous_range) == number:
                    range_found = True
                    break
            if range_found:
                print(f"Contigous Range giving number : {contiguous_range}")
                print(f"Code Weakness : {np.min(contiguous_range) + np.max(contiguous_range)}")
                break
            else:
                contiguous_range_size += 1
        break
