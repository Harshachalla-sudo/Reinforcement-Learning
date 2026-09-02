# EX39: Healthcare Resource Management

patients = ["Patient1", "Patient2", "Patient3"]

resources = [5,3,4]

reward = 0

print("Healthcare Management\n")

for i in range(len(patients)):

    print(patients[i])
    print("Resources Allocated =", resources[i])

    reward += resources[i] * 10

    print()

print("Total Reward =", reward)
