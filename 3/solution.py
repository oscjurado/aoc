import os 
with open("input.txt", "r") as file:
    input = file.readlines()
lines = [line.strip() for line in input]

counter = 0

for line in lines:
    highest = line[0]
    for char in line[:-1]:
        if int(char) > int(highest):
            highest = char
        place = line.find(highest) + 1
        new_line = line[place:]
    second_highest = new_line[0]
    for char in new_line:
        if int(char) > int(second_highest):
            second_highest = char
    value = int(highest + second_highest)
    counter += value
    print("line is: " + str(lines.index(line)+1))
    print(value)
    print(counter)

