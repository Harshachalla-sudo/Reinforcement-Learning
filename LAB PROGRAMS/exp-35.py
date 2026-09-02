# EX35: Value Equivalence Prediction

portfolios = {
    "Portfolio A": 120000,
    "Portfolio B": 145000,
    "Portfolio C": 138000
}

print("Investment Portfolio Analysis\n")

best_portfolio = ""
highest = 0

for portfolio in portfolios:

    print(portfolio, "Predicted Value = Rs.", portfolios[portfolio])

    if portfolios[portfolio] > highest:
        highest = portfolios[portfolio]
        best_portfolio = portfolio

print("\nBest Portfolio =", best_portfolio)
print("Highest Predicted Value = Rs.", highest)
