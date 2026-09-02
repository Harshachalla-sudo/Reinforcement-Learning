import random

ads = [0, 0, 0]
count = [0, 0, 0]
epsilon = 0.2

for i in range(100):

    if random.random() < epsilon:
        ad = random.randint(0, 2)
    else:
        ad = ads.index(max(ads))

    reward = random.randint(0, 1)  

    count[ad] += 1
    ads[ad] += (reward - ads[ad]) / count[ad]

print("Click Rates:", ads)
print("Best Advertisement:", ads.index(max(ads)))
