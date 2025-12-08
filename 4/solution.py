import os 
with open("input.txt", "r") as file:
    input = [line.strip() for line in file]
    

counter = 0
rows = len(input)
cols = len(input[0])

neighbors = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]

for r in range(rows):
    for c in range(rows):
        if input[r][c] !="@":
            continue
        adjacent = 0

        for dr, dc in neighbors:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if input[nr][nc] == "@":
                    adjacent += 1
        
        if adjacent < 4:
            counter += 1
print(counter)