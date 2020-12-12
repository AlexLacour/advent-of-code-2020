"""Joltage and adapters : find a chain using every adapter to connect your device to the outlet.
"""
import os
import copy
import numpy as np
from itertools import combinations
from collections import defaultdict
from multiprocessing import Pool

adapters_jolts_raw = open("inputs/day10_input.txt", "r").readlines()
adapters_jolts = [int(adapter.replace("\n", "")) for adapter in adapters_jolts_raw]

builtin_joltage = np.max(adapters_jolts) + 3
outlet_joltage = 0
adapters_jolts.append(outlet_joltage)
adapters_jolts.append(builtin_joltage)
first_chain = sorted(adapters_jolts)


def get_jolts_variations(chain):
    variations_used = defaultdict(int)

    for adapter_id, (adapter_jolt, next_adapter_jolt) in enumerate(zip(chain, chain[1:])):
        variation = next_adapter_jolt - adapter_jolt
        variations_used[variation] += 1
    return variations_used


def get_disposable_values(chain):
    disposable_values = []
    for adapter_jolt, next_adapter_jolt, next2_adapter_jolt in zip(chain, chain[1:], chain[2:]):
        variation = next_adapter_jolt - adapter_jolt
        next_variation = next2_adapter_jolt - adapter_jolt
        if variation <= 3 and next_variation <= 3:
            disposable_values.append(next_adapter_jolt)

    return disposable_values


def is_chain_valid(chain, disposable_values):
    chain2 = copy.copy(chain)
    for val in disposable_values:
        chain2.remove(val)
    variations = get_jolts_variations(chain2)

    if max(variations.keys()) <= 3:
        return True
    return False


variations_used = get_jolts_variations(chain=first_chain)
print(f"Result of the chain : {variations_used[1] * variations_used[3]}")

all_disposable_values = []
chain = copy.copy(first_chain)
while True:
    old_len = len(chain)
    disposable_values = get_disposable_values(chain=chain)
    all_disposable_values.append(disposable_values)

    for val in disposable_values:
        chain.remove(val)
    new_len = len(chain)
    if old_len == new_len:
        break
disposable_values = list(set([val for arr in all_disposable_values for val in arr]))


invalid_combis = []
total_num_chains = 0
for combi_len in range(0, len(disposable_values), 1):
    print(f"Processing combination length : {combi_len}...")

    for combination in combinations(disposable_values, r=combi_len):
        valid_combi = True
        for wrong_one in invalid_combis:
            if wrong_one.issubset(sorted(combination)):
                valid_combi = False
                break
        if valid_combi:
            if is_chain_valid(first_chain, combination):
                total_num_chains += 1
            else:
                invalid_combis.append(set(sorted(combination)))

print(f"Number of possible chains : {total_num_chains}")
