# EX31: SARSA Algorithm

states = ["Start", "Player Move", "Computer Move", "Win"]

Q = {
    "Start": 0,
    "Player Move": 0,
    "Computer Move": 0,
    "Win": 0
}

alpha = 0.5
gamma = 0.9

print("SARSA Learning\n")

for episode in range(10):

    state = "Start"

    while state != "Win":

        if state == "Start":
            next_state = "Player Move"
            reward = 5

        elif state == "Player Move":
            next_state = "Computer Move"
            reward = 8

        else:
            next_state = "Win"
            reward = 15

        Q[state] = Q[state] + alpha * (
            reward + gamma * Q[next_state] - Q[state]
        )

        print(state, "->", next_state,
              "Q =", round(Q[state], 2))

        state = next_state

print("\nFinal Q Values")

for s in states:
    print(s, "=", round(Q[s], 2))
