"""Fix the booting code.
"""

from os import replace


instructions_raw = open("inputs/day8_input.txt", "r").readlines()
instructions = [instruction.replace("\n", "") for instruction in instructions_raw]

def boot(replace_id=0):
    accumulator = 0
    instructions_done = []

    instruction_id = 0
    while True:
        instruction_todo = instructions[instruction_id]
        action, value = instruction_todo.split(" ")
        if replace_id == instruction_id and replace_id != 0:
            if action == 'jmp':
                action = 'nop'
            elif action == 'nop':
                action = 'jmp'
            elif action == 'acc':
                print("You got the wrong problematic id...")
                break

        if instruction_id in instructions_done:
            problematic_instruction = instructions_done[-1]
            boot(replace_id=problematic_instruction)
            break

        instructions_done.append(instruction_id)

        if action == 'acc':
            accumulator += int(value)
            instruction_id += 1
        elif action == 'jmp':
            instruction_id += int(value)
        elif action == 'nop':
            instruction_id += 1
        
        if instruction_id >= len(instructions):
            break

    fixed_str = "Real " if replace_id != 0 else ""
    print(f"{fixed_str}Accumulator value : {accumulator}")


boot()
