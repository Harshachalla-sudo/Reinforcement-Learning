# EX38: POMDP Robot Navigation

states = ["Start", "Unknown Area", "Target"]

belief = 0.50

print("POMDP Navigation\n")

for state in states:

    belief += 0.15

    print("State :", state)
    print("Belief =", round(belief,2))
    print()

print("Target Reached")
