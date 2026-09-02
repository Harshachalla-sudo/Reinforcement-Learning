# EX21: Model-Based Reinforcement Learning

states = ["Start", "Room A", "Room B", "Goal"]

model = {
    "Start": "Room A",
    "Room A": "Room B",
    "Room B": "Goal"
}

reward = {
    "Room A": 5,
    "Room B": 10,
    "Goal": 20
}

state = "Start"
total_reward = 0

print("Model-Based Reinforcement Learning\n")

while state != "Goal":

    print("Current State:", state)

    state = model[state]

    print("Next State:", state)

    total_reward += reward[state]

    print("Reward:", reward[state])
    print()

print("Goal Reached")
print("Total Reward =", total_reward)
