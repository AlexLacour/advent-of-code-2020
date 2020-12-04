"""Detect invalid passports
"""
import numpy as np

passports_data = open("inputs/day4_input.txt", "r").read()
proposed_passports = passports_data.split("\n\n")
proposed_passports = [proposed_passport.replace("\n", " ").split(" ") for proposed_passport in proposed_passports]

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def are_required_keys_present(passport_keys):
    for required_key in required_keys:
        if not (required_key in passport_keys):
            return False
    return True


def is_keyvalue_valid(key, value):
    if key == 'byr':
        if not (len(value) == 4 and value.isdigit() and int(value) >= 1920 and int(value) <= 2002):
            return False
    elif key == 'iyr':
        if not (len(value) == 4 and value.isdigit() and int(value) >= 2010 and int(value) <= 2020):
            return False
    elif key == 'eyr':
        if not (len(value) == 4 and value.isdigit() and int(value) >= 2020 and int(value) <= 2030):
            return False
    elif key == 'hgt':
        if value[-2:] == 'cm':
            if not (int(value[0:-2]) >= 150 and int(value[0:-2]) <= 193):
                return False
        elif value[-2:] == 'in':
            if not (int(value[0:-2]) >= 59 and int(value[0:-2]) <= 76):
                return False
        else:
            return False
    elif key == 'hcl':
        if not (value[0] == "#"):
            return False
        else:
            for char in value:
                if char.isdigit():
                    if not (int(char) in range(10)):
                        return False
                elif char.isalpha():
                    if not (char in 'abcdef'):
                        return False
    elif key == 'ecl':
        if not (value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
            return False
    elif key == 'pid':
        if not (len(value) == 9 and value.isdigit()):
            return False
    return True


def is_passport_valid(passport):
    keys_presence = are_required_keys_present(passport.keys())
    if keys_presence:
        for key, value in passport.items():
            if not is_keyvalue_valid(key, value):
                return False
    return keys_presence


present_keys_per_password = [
    {element.split(":")[0]: element.split(":")[1] for element in proposed_passport if element != ''}
    for proposed_passport in proposed_passports
]

required_keys_presence = [
    int(is_passport_valid(passport)) for passport in present_keys_per_password
]

print(f"Number of valid passports : {np.sum(required_keys_presence)}")
