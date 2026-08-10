# 3 x 3 Grid World
grid = [
    [0, 0, 0],
    [0, 1, 0],   # 1 = Obstacle
    [0, 0, 2]    # 2 = Goal
]

# Starting position
row = 0
col = 0

print("Grid World")
for r in grid:
    print(r)

print("\nRobot Path:")

# Simple policy: Move Right first, then Down
while grid[row][col] != 2:

    if col < 2 and grid[row][col + 1] != 1:
        col += 1
    elif row < 2 and grid[row + 1][col] != 1:
        row += 1

    print("(", row, ",", col, ")")

print("\nGoal Reached!")
