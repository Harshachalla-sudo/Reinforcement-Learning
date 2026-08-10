import gym

# Create MountainCar environment
env = gym.make("MountainCar-v0")

# Reset environment
state = env.reset()

print("Starting MountainCar Simulation")

# Run for 20 steps
for i in range(20):

    # Choose a random action
    action = env.action_space.sample()

    # Perform the action
    state, reward, done, info = env.step(action)

    print("Step:", i + 1)
    print("Action:", action)
    print("Reward:", reward)

    if done:
        print("Goal Reached!")
        break

env.close()
