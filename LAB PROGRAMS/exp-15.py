import random

episodes = 100
total_time = 0

# Simulate 100 customer calls
for i in range(episodes):

    # Randomly assign a representative
    representative = random.choice(["Junior", "Senior"])

    # Call handling time (minutes)
    if representative == "Senior":
        time = random.randint(3, 5)   # Faster
    else:
        time = random.randint(6, 10)  # Slower

    total_time += time

# Average handling time
average_time = total_time / episodes

print("Total Calls:", episodes)
print("Average Call Handling Time:", average_time, "minutes")exp-
