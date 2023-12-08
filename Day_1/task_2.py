# Open file and read lines
file1 = open('input_1.txt', 'r')
lines = file1.readlines()

zero = "zero"
one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight = "eight"
nine = "nine"

numbers = [zero, one, two, three, four, five, six, seven, eight, nine]

sum = 0
line = ""

for line in lines:
    line = line.replace("\n", "")
    formatted_line = line

    numbers_in_line = {}
    for number_int, number_str in enumerate(numbers):
    # change "numbers" to numbers
        index = line.find(number_str)
        if index >= 0:
            numbers_in_line[index] = number_int
        index = line.rfind(number_str)
        if index >= 0:
            numbers_in_line[index] = number_int

    numbers_in_line = dict(sorted(numbers_in_line.items(), key=lambda item: item[0], reverse=True))
    for index, number_int in numbers_in_line.items():
        # add numbers to correct positions
        formatted_line = formatted_line[:index] + str(number_int) + formatted_line[index:]

    for char in formatted_line:
        # if char is a letter, delete it
        if char.isalpha():
            formatted_line = formatted_line.replace(char, "")
    
    if len(formatted_line) == 1:
    # if there is only 1 number in line
        line_value = str(formatted_line[0]) + str(formatted_line[0])
        sum = sum + int(line_value)

    else:
    # if multiple numbers in line
        first_number = str(formatted_line[0])
        last_number = str(formatted_line[-1])
        line_value = first_number + last_number
        sum = sum + int(line_value)

print(sum)