"""What is the Manhattan distance between that location and the ship's starting position?
"""
import numpy as np

navigation_data_raw = open("inputs/day12_input.txt", "r").readlines()

navigation_data = [(instruction[0], int(instruction[1:].replace("\n", ""))) for instruction in navigation_data_raw]

position = {
    'east': 0,
    'south': 0,
    'west': 0,
    'north': 0
}

waypoint_position = [
    10,  # east
    0,  # south
    0,  # west
    1  # north
]

angles = ["east", "south", "west", "north"]
facing = 0

for instruction_type, instruction_value in navigation_data:
    if instruction_type == "N":
        waypoint_position[3] += instruction_value
    elif instruction_type == "S":
        waypoint_position[1] += instruction_value
    elif instruction_type == "E":
        waypoint_position[0] += instruction_value
    elif instruction_type == "W":
        waypoint_position[2] += instruction_value

    elif instruction_type == "L":
        turning_val = instruction_value // 90
        # facing = (facing - turning_val) % len(angles)
        for _ in range(turning_val):
            waypoint_position = np.roll(waypoint_position, -1)
    elif instruction_type == "R":
        turning_val = instruction_value // 90
        # facing = (facing + turning_val) % len(angles)
        for _ in range(turning_val):
            waypoint_position = np.roll(waypoint_position, 1)
    elif instruction_type == "F":
        position["east"] += waypoint_position[0] * instruction_value
        position["south"] += waypoint_position[1] * instruction_value
        position["west"] += waypoint_position[2] * instruction_value
        position["north"] += waypoint_position[3] * instruction_value

manhattan_distance = abs(position["north"] - position["south"]) + abs(position["east"] - position["west"])
print(f"Manhattan Distance of the ferry : {manhattan_distance}")
