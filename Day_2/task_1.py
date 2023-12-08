import re

file1 = open('Day_2/input_2.txt', 'r')
lines = file1.readlines()

sum = 0
cubes_in_bag = {
    "red": 12,
    "green": 13,
    "blue": 14
    }

def check_line(line):

    game_id, sets = line.split(":")
    game_id = re.sub('\D', '', game_id)
    sets = sets.split(";")

    # 2. Go through sets
    for set in sets:
        colors = set.split(",")

        # 3. Go through colors of cubes
        for dice in colors:
            dice = dice.replace(" ", "")
            dice_color = re.sub('\d', '', dice)
            dice_number = re.sub('\D', '', dice)

            # 4. Check if color is in cubes_in_bag
            for color_limit in cubes_in_bag:
                if color_limit == dice_color:
                    if cubes_in_bag[color_limit] < int(dice_number):
                        return 0
            
    return int(game_id)

# 1. Go through lines
for line in lines:
    line = line.replace("\n", "")

    sum = sum + check_line(line)
print(sum)