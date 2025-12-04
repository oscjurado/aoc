import os 
with open("input.txt", "r") as file:
    input = file.readlines()

start = 50
counter = 0


for line in input:
    direction = line[0]
    distance = int(line[1:])

    step = -1 if direction == "L" else 1

    for click in range(distance):
        start = (start + step) % 100
        if start == 0:
            counter+= 1

print(counter) 