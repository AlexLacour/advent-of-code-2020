"""Find the number of yes-answered questions
"""
import numpy as np
from collections import Counter

answers_raw = open("inputs/day6_input.txt", "r").read().split("\n\n")

answers = [set(group_answers.replace("\n", "")) for group_answers in answers_raw]
num_answers = [len(yes_answers) for yes_answers in answers]
print(f"Total yes-answered questions : {np.sum(num_answers)}")

answers2 = [group_answers.split("\n") for group_answers in answers_raw]

total_yes = 0
for yes_answers in answers2:
    num_people_in_group = len([answer for answer in yes_answers if answer != ''])
    full_string = "".join(answer for answer in yes_answers)
    char_occurences = Counter(full_string)
    
    for count in char_occurences.values():
        if count == num_people_in_group:
            total_yes += 1

print(f"Total everyone-answered-yes questions : {total_yes}")
