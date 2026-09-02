# EX30: Deep Q-Network (DQN) Simulation

states = ["Highway", "Traffic", "Destination"]

weights = [0.50, 0.80]

print("Deep Q-Network Simulation\n")

for epoch in range(1, 11):

    weights[0] += 0.05
    weights[1] += 0.04

    print("Epoch", epoch)
    print("Highway Weight =", round(weights[0], 2))
    print("Traffic Weight =", round(weights[1], 2))
    print()

print("Training Completed")
