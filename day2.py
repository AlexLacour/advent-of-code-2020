"""Find invalid passwords in the list.
"""
import numpy as np

def policy1_is_valid(password):
    min_max, req_char, password_str = password.replace("\n", "").split(" ")
    req_char = req_char.replace(":", "")
    min_val = int(min_max.split("-")[0])
    max_val = int(min_max.split("-")[1])
    n_occurences_req_char = password_str.count(req_char)
    valid = (n_occurences_req_char <= max_val) and (n_occurences_req_char >= min_val)
    return valid


def policy2_is_valid(password):
    min_max, req_char, password_str = password.replace("\n", "").split(" ")
    req_char = req_char.replace(":", "")
    first_index = int(min_max.split("-")[0]) - 1
    second_index = int(min_max.split("-")[1]) - 1

    first_char = password_str[first_index]
    sec_char = password_str[second_index]

    first_char_presence = first_char == req_char
    sec_char_presence = sec_char == req_char

    return (first_char_presence or sec_char_presence) and not (first_char_presence and sec_char_presence)

passwords = open("inputs/day2_input.txt", "r").readlines()

res1 = [int(policy1_is_valid(password)) for password in passwords]
res2 = [int(policy2_is_valid(password)) for password in passwords]

n_valid_passwords = np.sum(res2)
print(f"Number of valid passwords : {n_valid_passwords}")
