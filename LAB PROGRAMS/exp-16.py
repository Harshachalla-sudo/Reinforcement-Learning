# Grid (3x3)
# S = Start, G = Goal, X = Obstacle

grid = [
    ["S", ".", "."],
    [".", "X", "."],
    [".", ".", "G"]
]

# State values
value = [
    [0, 0, 0],
    [0, -1, 0],   # -1 represents obstacle
    [0, 0, 10]    # Goal value = 10
]

# Bellman Update (Value Iteration)
for k in range(5):
    for i in range(3):
        for j in range(3):

            if grid[i][j] == "X" or grid[i][j] == "G":
                continue

            neighbors = []

            if i > 0 and value[i-1][j] != -1:
                neighbors.append(value[i-1][j])
            if i < 2 and value[i+1][j] != -1:
                neighbors.append(value[i+1][j])
            if j > 0 and value[i][j-1] != -1:
                neighbors.append(value[i][j-1])
            if j < 2 and value[i][j+1] != -1:
                neighbors.append(value[i][j+1])

            value[i][j] = max(neighbors) - 1

print("State Value Function:")
for row in value:
    print(row)

print("\nOptimal Path:")
print("(0,0) → (0,1) → (0,2) → (1,2) → (2,2)")
