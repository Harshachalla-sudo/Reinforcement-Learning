import random

money = 100
stock = 0

for day in range(10):
    action = random.choice(["Buy", "Sell", "Hold"])
    price = random.randint(10, 20)

    if action == "Buy" and money >= price:
        stock += 1
        money -= price

    elif action == "Sell" and stock > 0:
        stock -= 1
        money += price

    print("Day", day+1, "|", action, "| Price:", price)

print("Money Left:", money)
print("Stocks:", stock)
