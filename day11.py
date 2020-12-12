"""Where to sit in the waiting area : floor ., seat empty L, seat taken #
"""
import copy
import numpy as np

seats_data_raw = open("inputs/day11_input.txt", "r").readlines()
seats_data = [row.replace("\n", "") for row in seats_data_raw]

# seats_data = [
#     "L.LL.LL.LL",
#     "LLLLLLL.LL",
#     "L.L.L..L..",
#     "LLLL.LL.LL",
#     "L.LL.LL.LL",
#     "L.LLLLL.LL",
#     "..L.L.....",
#     "LLLLLLLLLL",
#     "L.LLLLLL.L",
#     "L.LLLLL.LL"
# ]

def get_occupied_places(data, row_id, place_id):
    nearby_places = []

    # rule 1
    if place_id != 0:
        nearby_places.append(data[row_id][place_id - 1])
    if place_id != len(data[0]) - 1:
        nearby_places.append(data[row_id][place_id + 1])

    if row_id != len(data) - 1:
        nearby_places.append(data[row_id + 1][place_id])
    if row_id != len(data) - 1 and place_id != 0:
        nearby_places.append(data[row_id + 1][place_id - 1])
    if row_id != len(data) - 1 and place_id != len(data[0]) - 1:
        nearby_places.append(data[row_id + 1][place_id + 1])

    if row_id != 0:
        nearby_places.append(data[row_id - 1][place_id])
    if row_id != 0 and place_id != 0:
        nearby_places.append(data[row_id - 1][place_id - 1])
    if row_id != 0 and place_id != len(data[0]) - 1:
        nearby_places.append(data[row_id - 1][place_id + 1])

    n_occupied = 0
    for place in nearby_places:
        if place == "#":
            n_occupied += 1
    return n_occupied


def look_at(data, row_id, place_id, direction):
    position_x = row_id
    position_y = place_id
    while True:
        position_x += direction[0]
        position_y += direction[1]

        if position_x < 0 or position_x >= len(data):
            break
        if position_y < 0 or position_y >= len(data[0]):
            break

        if data[position_x][position_y] in ["L", "#"]:
            return data[position_x][position_y]

    return "."


def get_occupied_places2(data, row_id, place_id):
    nearby_places = []

    # rule 2
    if place_id != 0:
        nearby_places.append(look_at(data, row_id, place_id, [0, -1]))
    if place_id != len(data[0]) - 1:
        nearby_places.append(look_at(data, row_id, place_id, [0, 1]))

    if row_id != len(data) - 1:
        nearby_places.append(look_at(data, row_id, place_id, [1, 0]))
    if row_id != len(data) - 1 and place_id != 0:
        nearby_places.append(look_at(data, row_id, place_id, [1, -1]))
    if row_id != len(data) - 1 and place_id != len(data[0]) - 1:
        nearby_places.append(look_at(data, row_id, place_id, [1, 1]))

    if row_id != 0:
        nearby_places.append(look_at(data, row_id, place_id, [-1, 0]))
    if row_id != 0 and place_id != 0:
        nearby_places.append(look_at(data, row_id, place_id, [-1, -1]))
    if row_id != 0 and place_id != len(data[0]) - 1:
        nearby_places.append(look_at(data, row_id, place_id, [-1, 1]))

    n_occupied = 0
    for place in nearby_places:
        if place == "#":
            n_occupied += 1

    return n_occupied


seat_tolerance = 5
n_steps = 0
while True:
    temp_data = []
    for row_id, seat_row in enumerate(seats_data):
        temp_row = []
        for place_id, place in enumerate(seat_row):
            if place == "L" and get_occupied_places2(seats_data, row_id, place_id) == 0:
                temp_row.append("#")
            elif place == "#" and get_occupied_places2(seats_data, row_id, place_id) >= seat_tolerance:
                temp_row.append("L")
            else:
                temp_row.append(place)
        temp_data.append(temp_row)
    n_steps += 1

    array_diff = False
    for row, temp_row in zip(seats_data, temp_data):
        for place, temp_place in zip(row, temp_row):
            if place != temp_place:
                array_diff = True

    if not array_diff:
        print(f"Chaos stabilized after {n_steps} steps")
        break
    seats_data = temp_data


n_occupied = 0
for row in seats_data:
    for place in row:
        if place == "#":
            n_occupied += 1

print(f"Number of occupied places : {n_occupied}")
