import random
contents = ["Content A", "Content B"]
reward = {
    "Content A": 0,
    "Content B": 0
}
count = {
    "Content A": 0,
    "Content B": 0
}
epsilon = 0.2
for i in range(100):
    if random.random() < epsilon:
        choice = random.choice(contents)   
    else:
        choice = max(reward, key=reward.get)  

    if choice == "Content A":
        user_reward = random.randint(1, 5)
    else:
        user_reward = random.randint(3, 8)

    count[choice] += 1
    reward[choice] = reward[choice] + (user_reward - reward[choice]) / count[choice]


print("Content Values:")
for c in contents:
    print(c, ":", round(reward[c], 2))

best_content = max(reward, key=reward.get)

print("\nRecommended Content:", best_content)
