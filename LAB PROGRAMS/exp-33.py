# EX33: DDPG Simulation

resources = 0
units = 0
reward = 0

print("DDPG Strategy Game\n")

for episode in range(1, 11):

    resources += 10
    units += 2
    reward += resources + units

    print("Episode", episode)
    print("Resources =", resources)
    print("Units Built =", units)
    print("Reward =", reward)
    print()

print("Training Completed")
