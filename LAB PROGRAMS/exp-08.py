
road = [
    ["S", ".", "."],
    [".", "X", "."],
    [".", ".", "G"]
]

row = 0
col = 0

print("Autonomous Car Navigation\n")

while road[row][col] != "G":

    print("Car at:", (row, col))
    if col < 2 and road[row][col + 1] != "X":
        col += 1
    elif row < 2 and road[row + 1][col] != "X":
        row += 1
    else:
        print("Obstacle! Finding another path.")
        break

print("Car at:", (row, col))
print("Destination Reached Successfully!")
