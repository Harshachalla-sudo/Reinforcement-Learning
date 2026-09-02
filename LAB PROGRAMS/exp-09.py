import random

# Two policies
def random_policy():
    return random.choice(["Junior", "Senior"])

def senior_policy():
    return "Senior"

# Run one simulation
def simulate(policy, episodes):
    total_reward = 0

    for i in range(episodes):
        worker = policy()

        if worker == "Senior":
            reward = random.randint(8, 10)
        else:
            reward = random.randint(4, 6)

        total_reward += reward

    average = total_reward / episodes
    return average

episodes = 100

print("Random Policy Value :", simulate(random_policy, episodes))
print("Senior Policy Value :", simulate(senior_policy, episodes))
