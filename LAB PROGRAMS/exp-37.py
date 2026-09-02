# EX37: Cooperative Multi-Agent Reinforcement Learning

agents = ["Agent A", "Agent B", "Agent C"]

tasks = ["Search Area", "Collect Object", "Deliver Object"]

rewards = [10, 15, 20]

total_reward = 0

print("Cooperative Multi-Agent Reinforcement Learning\n")

for i in range(len(agents)):

    print("Agent :", agents[i])
    print("Task  :", tasks[i])
    print("Reward:", rewards[i])
    print()

    total_reward += rewards[i]

print("All Agents Completed Their Tasks")
print("Total Reward =", total_reward)

best_agent = agents[rewards.index(max(rewards))]

print("Best Performing Agent =", best_agent)
