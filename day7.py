"""Find how many luggages colors can contain the shiny gold one.
"""
from collections import defaultdict

luggages_rules_raw = open("inputs/day7_input.txt", "r").readlines()

luggages_rules = [
    luggage_rule.replace("\n", "").replace("bags", "").replace(" ", "").replace(".", "").replace("bag", "").split("contain")
    for luggage_rule in luggages_rules_raw
]

target_colors = ["shinygold"]
colors_leading_to_gold = defaultdict(bool)
for target_color in target_colors:
    for rule in luggages_rules:
        container = rule[0]
        contained = [contained_type[1:] if contained_type[0].isdigit() else contained_type for contained_type in rule[1].split(",")]
        if target_color in contained:
            colors_leading_to_gold[container] = True
            if container not in target_colors:
                target_colors.append(container)

print(f"Number of Bag-colors leading eventually to gold : {len(colors_leading_to_gold)}")

target_containers = [("shinygold", 1)]
total_contained = 0
for target_container, mul in target_containers:
    for rule in luggages_rules:
        container = rule[0]

        contained = []
        for contained_type in rule[1].split(","):
            if contained_type[0].isdigit():
                contained.append((contained_type[1:], int(contained_type[0])))
            else:
                contained.append((contained_type, 0))
        if target_container == container:
            for contained_color, number_of_bags in contained:
                total_contained += number_of_bags * mul
                if contained_color not in target_containers:
                    target_containers.append((contained_color, number_of_bags * mul))

print(f"Total number of bags contained : {total_contained}")
