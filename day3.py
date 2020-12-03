"""How many trees are encountered by taking the toboggan into the forest ?
"""
import numpy as np

forest = open("inputs/day3_input.txt", "r").readlines()
forest = [row.replace("\n", "") for row in forest]

tree_str = "#"
toboggan_slopes = [
    {"right": 1, "down": 1},
    {"right": 3, "down": 1},
    {"right": 5, "down": 1},
    {"right": 7, "down": 1},
    {"right": 1, "down": 2}
]

def get_number_of_trees_uncountered(slope_dict):
    init_player_pos = [0, 0]
    number_of_trees = 0
    player_pos = init_player_pos

    while player_pos[0] < len(forest):
        tree_presence = forest[player_pos[0]][player_pos[1]] == tree_str
        number_of_trees += int(tree_presence)
        player_pos[0] += slope_dict["down"]
        player_pos[1] = (player_pos[1] + slope_dict["right"]) % len(forest[0])

    print(f"Trees encountered : {number_of_trees}")
    return number_of_trees

tree_values = [get_number_of_trees_uncountered(slope_dict) for slope_dict in toboggan_slopes]
total_val = 1
for tree_value in tree_values:
    total_val *= tree_value
print(f"Multiplication Result {total_val}")
