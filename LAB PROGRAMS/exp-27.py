# EX27: Autonomous Car Navigation

roads = ["Start", "Junction", "Signal", "Destination"]

policy = {
    "Start": "Go Straight",
    "Junction": "Turn Left",
    "Signal": "Stop and Go",
    "Destination": "Reached"
}

reward = {
    "Start": 5,
    "Junction": 10,
    "Signal": 15,
    "Destination": 20
}

total_reward = 0

print("Autonomous Car Navigation\n")

for road in roads:
    print("Location :", road)
    print("Action   :", policy[road])
    print("Reward   :", reward[road])
    print()

    total_reward += reward[road]

print("Destination Reached Successfully")
print("Total Reward =", total_reward)
