# EX23: Intelligent Traffic Signal Control

signals = ["North", "South", "East", "West"]

vehicles = {
    "North": 25,
    "South": 18,
    "East": 30,
    "West": 12
}

green_signal = max(vehicles, key=vehicles.get)

print("Traffic Signal Status\n")

for signal in signals:
    print(signal, "Road Vehicles =", vehicles[signal])

print("\nGreen Signal Given To:", green_signal)
print("Vehicles Cleared =", vehicles[green_signal])
