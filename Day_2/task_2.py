import re

file1 = open('Day_2/input_2.txt', 'r')
lines = file1.readlines()

sum = 0

def check_line(line):

    colors_in_bag ={
        "red": [],
        "green": [],
        "blue": []
    } 
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
            for color in colors_in_bag:
                if color == dice_color:
                    colors_in_bag[color].append(int(dice_number))
    
    power_of_colors = 1
    for color in colors_in_bag:
        colors_in_bag[color] = max(colors_in_bag[color])
        power_of_colors = power_of_colors * int(colors_in_bag[color])
    
    return power_of_colors    

# 1. Go through lines
for line in lines:
    line = line.replace("\n", "")

    sum = sum + check_line(line)

print(sum)