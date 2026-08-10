import random

rooms = 5
cleaned = 0
energy = 20

for i in range(rooms):
    action = random.choice(["Clean", "Move"])

    if action == "Clean":
        cleaned += 1
        energy -= 2
    else:
        energy -= 1

print("Rooms Cleaned:", cleaned)
print("Energy Left:", energy)
