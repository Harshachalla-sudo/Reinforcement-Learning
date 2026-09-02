# EX22: Offline Reinforcement Learning

patients = [
    {"Name": "Patient1", "Treatment": "Medicine A", "Reward": 80},
    {"Name": "Patient2", "Treatment": "Medicine B", "Reward": 90},
    {"Name": "Patient3", "Treatment": "Medicine C", "Reward": 75},
    {"Name": "Patient4", "Treatment": "Medicine B", "Reward": 95}
]

best_patient = ""
best_treatment = ""
best_reward = -1

print("Offline Reinforcement Learning\n")

for patient in patients:

    print("Patient :", patient["Name"])
    print("Treatment :", patient["Treatment"])
    print("Reward :", patient["Reward"])
    print()

    if patient["Reward"] > best_reward:
        best_reward = patient["Reward"]
        best_patient = patient["Name"]
        best_treatment = patient["Treatment"]

print("Best Treatment Recommendation")
print("Patient :", best_patient)
print("Treatment :", best_treatment)
print("Maximum Reward :", best_reward)
