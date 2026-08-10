import random

# Actions (Machine Settings)
actions = ["Low", "Medium", "High"]

# Value function for each action
value = {"Low": 0, "Medium": 0, "High": 0}

# Number of times each action is selected
count = {"Low": 0, "Medium": 0, "High": 0}

# Simulate 10 production cycles
for i in range(10):

    # Policy: Randomly choose a machine setting
    action = random.choice(actions)

    # Environment: Reward based on product quality
    if action == "Low":
        reward = random.randint(2, 4)
    elif action == "Medium":
        reward = random.randint(5, 7)
    else:
        reward = random.randint(8, 10)

    # Update value function
    count[action] += 1
    value[action] = value[action] + (reward - value[action]) / count[action]

    print("Cycle:", i + 1)
    print("Machine Setting:", action)
    print("Reward:", reward)
    print()

print("Value Function:")
for action in actions:
    print(action, "=", round(value[action], 2))
