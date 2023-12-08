file1 = open('Day_1/input_1.txt', 'r')
lines = file1.readlines()

sum = 0
line = ""

for line in lines:
    line = line.replace("\n", "")

    for char in line:
        if char.isalpha():
            line = line.replace(char, "")

    if len(line) == 1:
        line_value = str(line[0]) + str(line[0])
        sum = sum + int(line_value)

    else:
        first_number = str(line[0])
        last_number = str(line[-1])
        line_value = first_number + last_number
        sum = sum + int(line_value)

print(sum)