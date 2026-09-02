# EX32: Dueling DQN Simulation

states = ["Start", "Obstacle", "Goal"]

value = 0.5
advantage = 0.3

print("Dueling DQN Simulation\n")

for episode in range(1, 11):

    value += 0.05
    advantage += 0.04

    q_value = value + advantage

    print("Episode", episode)
    print("Value =", round(value, 2))
    print("Advantage =", round(advantage, 2))
    print("Q Value =", round(q_value, 2))
    print()

print("Training Completed")
