import random
customers = 100

retained = 0
churned = 0
for i in range(customers):

    action = random.choice([0, 1])
    if action == 1:
        reward = 1     
        retained += 1
    else:
        reward = 0     
        churned += 1

retention_rate = retained / customers
churn_rate = churned / customers

print("Total Customers:", customers)
print("Customers Retained:", retained)
print("Customers Churned:", churned)

print("\nRetention Rate:", round(retention_rate, 2))
print("Churn Rate:", round(churn_rate, 2))
