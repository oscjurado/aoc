import os

with open("input.txt", "r") as file:
    input = file.readlines()


lines = input[0].split(',')
values = []
counter = 0
for line in lines:
    ints = []
    splitvalues = line.split('-')
    for num in splitvalues:
        ints.append(int(num))

    for i in range(ints[0], ints[1] + 1):
        if len(str(i)) % 2 == 0:
            first_part_end = len(str(i)) / 2
            first_part = str(i)[0:int(first_part_end)]
            last_part = str(i)[int(first_part_end):]
            if first_part == last_part:
                counter += i
    
print(counter)