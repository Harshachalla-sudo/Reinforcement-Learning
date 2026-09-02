# EX40: Personalized Learning

students = ["Student1","Student2","Student3"]

scores = [70,82,91]

print("Personalized Learning\n")

best_student = ""
highest = 0

for i in range(len(students)):

    print(students[i])
    print("Learning Score =", scores[i])
    print()

    if scores[i] > highest:
        highest = scores[i]
        best_student = students[i]

print("Best Learning Performance")
print("Student =", best_student)
print("Score =", highest)
