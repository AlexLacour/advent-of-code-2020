"""Find your seat in the plane.
"""
import numpy as np

seats_raw = [seat_data.replace("\n", "") for seat_data in open("inputs/day5_input.txt", "r").readlines()]

def find_row(seat_data):
    seat_row_data = seat_data[0:7]
    row = int(seat_row_data.replace("F", "0").replace("B", "1"), 2)
    return row

def find_col(seat_data):
    seat_col_data = seat_data[-3:]
    col = int(seat_col_data.replace("R", "1").replace("L", "0"), 2)
    return col

def get_seat_id(seat_data):
    row = find_row(seat_data)
    col = find_col(seat_data)
    seat_id = row * 8 + col
    return seat_id

seat_ids = [get_seat_id(seat_data) for seat_data in seats_raw]
max_id = np.max(seat_ids)

print(f"Maximum seat id : {max_id}")

all_ids = set(range(np.min(seat_ids), np.max(seat_ids) + 1))
seat_ids = set(seat_ids)

print(f"Your seat id is : {all_ids.difference(seat_ids)}")
