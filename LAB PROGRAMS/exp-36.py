# EX36: MAXQ Framework

tasks = ["Navigate", "Pick Object", "Deliver Object"]

reward = {
    "Navigate": 10,
    "Pick Object": 15,
    "Deliver Object": 20
}

total_reward = 0

print("MAXQ Hierarchical Reinforcement Learning\n")

for task in tasks:

    print("Task :", task)
    print("Reward :", reward[task])

    total_reward += reward[task]

    print()

print("All Tasks Completed")
print("Total Reward =", total_reward)
