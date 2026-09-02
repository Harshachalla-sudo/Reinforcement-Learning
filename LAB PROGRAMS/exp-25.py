# EX25: Bandit Algorithm Comparison

algorithms = {
    "Epsilon-Greedy": 78,
    "UCB": 85,
    "Thompson Sampling": 91
}

print("Advertisement Recommendation Results\n")

best = ""
highest = 0

for algo in algorithms:

    print(algo, "CTR =", algorithms[algo], "%")

    if algorithms[algo] > highest:
        highest = algorithms[algo]
        best = algo

print("\nBest Algorithm =", best)
print("Highest CTR =", highest, "%")
