# EX28: Bellman Optimality Equation

gamma = 0.9

states = ["A", "B", "C", "Goal"]

V = {
    "Goal": 100,
    "C": 0,
    "B": 0,
    "A": 0
}

reward = -1

for i in range(10):

    V["C"] = reward + gamma * V["Goal"]
    V["B"] = reward + gamma * V["C"]
    V["A"] = reward + gamma * V["B"]

print("Optimal State Values\n")

for state in states:
    print(state, "=", round(V[state], 2))

print("\nOptimal Path")
print("A -> B -> C -> Goal")
