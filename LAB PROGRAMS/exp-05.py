states = 5

reward = [0,0,0,0,10]

value = [0]*states

gamma = 0.9

for i in range(20):

    old = value.copy()

    for s in range(states-1):

        value[s] = max(
            reward[s]+gamma*old[min(s+1,4)],
            reward[s]+gamma*old[s]
        )

print("Optimal State Values")

for i in range(states):
    print("State",i,"=",round(value[i],2))
