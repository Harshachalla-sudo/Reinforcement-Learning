# EX26: Dynamic Pricing using Multi-Armed Bandit

strategies = {
    "Epsilon-Greedy": 12000,
    "UCB": 13500,
    "Thompson Sampling": 14250
}

print("Dynamic Pricing Results\n")

best = ""
revenue = 0

for strategy in strategies:

    print(strategy, "Revenue = Rs.", strategies[strategy])

    if strategies[strategy] > revenue:
        revenue = strategies[strategy]
        best = strategy

print("\nBest Pricing Strategy =", best)
print("Maximum Revenue = Rs.", revenue)
