states = 5
reward = [0, 1, 2, 3, 5]
gamma = 0.9

value = [0] * states

for i in range(20):
    for s in range(states - 2, -1, -1):
        value[s] = reward[s] + gamma * value[s + 1]

print("State Values")

for i in range(states):
    print("State", i, "=", round(value[i], 2))
