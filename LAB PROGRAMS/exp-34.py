# EX34: REINFORCE for Smart Home

temperature = 24
policy = 0.5
learning_rate = 0.05

print("Smart Home Temperature Control\n")

for day in range(1, 11):

    reward = 10

    policy += learning_rate

    if temperature > 22:
        temperature -= 1
    else:
        temperature += 1

    print("Day", day)
    print("Temperature =", temperature)
    print("Policy =", round(policy, 2))
    print()

print("Optimization Completed")
