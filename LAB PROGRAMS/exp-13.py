import random

score = 0

for step in range(10):
    move = random.choice(["Up", "Down", "Left", "Right"])

    if random.random() < 0.7:
        score += 10
        print(move, "- Food Collected")
    else:
        score -= 5
        print(move, "- Ghost Found")

print("Final Score:", score)
