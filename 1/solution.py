import os 
with open("input.txt", "r") as file:
    input = file.readlines()

start = 50
counter = 0

for line in input:
    diff = int(line[1:]) % 100
    print("going: " + str(line[0]))
    if line[0] == "L":
        if start > diff:
            print("start before looping is:" + str(start)+ " diff is:" + str(diff))
            start = start - diff
            print("start after is:" + str(start) )
            
        else:
            print("start before looping is:" + str(start) + " diff is:" + str(diff))
            start = (start + 100) - diff
            print("start after is:" + str(start))
            
    else:
        if start + diff > 100:
            print("start before looping is:" + str(start) + " diff is:" + str(diff))
            start = (start - 100) + diff
            print("start after is:" + str(start) )
        else:
            print("start before looping is:" + str(start) + " diff is:" + str(diff))
            start = start + diff
            print("start after is:" + str(start) )
    if start == 100:
        counter += 1    
    print(counter)
print(counter)
