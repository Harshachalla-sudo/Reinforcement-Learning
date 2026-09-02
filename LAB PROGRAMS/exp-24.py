# EX24: REINFORCE Algorithm

days = ["Day1", "Day2", "Day3", "Day4", "Day5"]

profits = [100, 150, 120, 180, 200]

policy = 0.5
learning_rate = 0.05

print("REINFORCE Trading System\n")

for i in range(len(days)):

    reward = profits[i]

    policy += learning_rate * reward / 100

    print(days[i])
    print("Profit =", reward)
    print("Policy =", round(policy, 2))
    print()

print("Final Policy =", round(policy, 2))
