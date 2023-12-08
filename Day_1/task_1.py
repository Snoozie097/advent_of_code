file1 = open('input_1.txt', 'r')
Lines = file1.readlines()


sum = 0
line = ""

for line in Lines:
    # Fix line spacing
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