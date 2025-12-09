import math
with open("input.txt") as file:
    input = file.readlines()



lines = []
for line in input:
    lines.append(line.split())

groups = [[row[i] for row in lines] for i in range(len(lines[0]))]
print(groups[0])

results = []
for group in groups:
    if group[-1] == "+":
        results.append(sum(int(x) for x in group[:4]))
    else:
        results.append(math.prod(int(x) for x in group[:4]))
    
total = 0

for result in results:
    total += result


print(total)