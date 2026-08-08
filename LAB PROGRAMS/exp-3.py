import random
import numpy as np

# --- Warehouse layout: shelves (S), packing station (P), obstacles (X) ---
GRID = [
    "..........",
    ".XX....S..",
    ".X.....X..",
    ".X.XXXXX..",
    ".X.X......",
    "...X.XXXX.",
    ".XXX......",
    "P.........",
]
ROWS, COLS = len(GRID), len(GRID[0])
SHELF = (1, 7)
STATION = (7, 0)
START = (0, 0)

MOVES = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right
ACTIONS = MOVES + ['pickup', 'dropoff']  # index 4,5

def is_free(pos):
    r, c = pos
    return 0 <= r < ROWS and 0 <= c < COLS and GRID[r][c] != 'X'

SLIP_PROB = 0.1  # chance movement doesn't go as commanded

def step(state, a_idx):
    pos, carrying = state

    if a_idx < 4:  # movement
        dr, dc = MOVES[a_idx]
        if random.random() < SLIP_PROB:
            dr, dc = random.choice(MOVES)  # slipped to a random direction
        nxt = (pos[0]+dr, pos[1]+dc)
        if not is_free(nxt):
            return (pos, carrying), -10, False   # collision, stay put
        return (nxt, carrying), -1, False

    elif a_idx == 4:  # pickup
        if pos == SHELF and not carrying:
            return (pos, True), 20, False
        return (pos, carrying), -1, False          # invalid pickup

    else:  # dropoff
        if pos == STATION and carrying:
            return (pos, False), 50, True           # delivery complete
        return (pos, carrying), -1, False           # invalid dropoff

# --- Q-learning agent ---
Q = np.zeros((ROWS, COLS, 2, len(ACTIONS)))

def choose_action(state, eps):
    if random.random() < eps:
        return random.randrange(len(ACTIONS))
    (r, c), carry = state
    return int(np.argmax(Q[r, c, int(carry)]))

def train(episodes=3000, alpha=0.2, gamma=0.95, eps_start=1.0, eps_min=0.05):
    eps = eps_start
    for ep in range(episodes):
        state = (START, False)
        for _ in range(300):
            a = choose_action(state, eps)
            nxt, r, done = step(state, a)
            (sr, sc), sc_carry = state
            (nr, nc), nc_carry = nxt
            best_next = 0 if done else np.max(Q[nr, nc, int(nc_carry)])
            idx = (sr, sc, int(sc_carry), a)
            Q[idx] += alpha * (r + gamma * best_next - Q[idx])
            state = nxt
            if done:
                break
        eps = max(eps_min, eps * 0.998)

train()

# --- Run learned policy ---
state = (START, False)
print(f"Start: {state}")
for i in range(50):
    (r, c), carry = state
    a = int(np.argmax(Q[r, c, int(carry)]))
    state, reward, done = step(state, a)
    label = ACTIONS[a] if a >= 4 else ['up','down','left','right'][a]
    print(f"step {i+1}: action={label}, state={state}, reward={reward}")
    if done:
        print("Delivery complete!")
        break