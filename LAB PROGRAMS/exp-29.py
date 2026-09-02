# EX29: Traffic Signal Optimization

signals = ["North", "South", "East", "West"]

vehicles = {
    "North": 30,
    "South": 18,
    "East": 25,
    "West": 12
}

print("Traffic Signal Optimization\n")

best_signal = max(vehicles, key=vehicles.get)

for signal in signals:
    print(signal, "Vehicles =", vehicles[signal])

print("\nOptimal Green Signal :", best_signal)
print("Maximum Vehicles Cleared :", vehicles[best_signal])
