import os

with open("input.txt") as file:
    input = [line.strip() for line in file]

ranges = []
nums = []
matches = set()

for entry in input:
    if entry.find("-") == -1:
       nums.append(entry)
    else:
       ranges.append((entry.rsplit("-")))

for num in nums:
    for range in ranges:
        if num == '' or range == '':
            continue
        elif int(range[0]) <= int(num) <= int(range[1]):
            print(num + " is in between " + range[0] + " and " + range[1])
            matches.add(num)

print(len(nums))
print(len(matches))