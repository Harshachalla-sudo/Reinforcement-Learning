import random
import numpy as np

# --- Environment: grid house with obstacles and a goal ---
GRID = [
    "..........",
    ".XX....X..",
    ".X.....X..",
    ".X.XXXXX..",
    ".X.X......",
    "...X.XXXX.",
    ".XXX......",
    "..........",
]
ROWS, COLS = len(GRID), len(GRID[0])
START = (0, 0)
GOAL = (7, 9)
ACTIONS = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

def is_free(pos):
    r, c = pos
    return 0 <= r < ROWS and 0 <= c < COLS and GRID[r][c] != 'X'

def step(state, action_idx):
    dr, dc = ACTIONS[action_idx]
    nxt = (state[0]+dr, state[1]+dc)
    if not is_free(nxt):
        nxt = state              # bumped into wall/obstacle, stay put
        reward = -5
    elif nxt == GOAL:
        reward = 100
    else:
        reward = -1               # small cost per step, encourages shortest path
    done = nxt == GOAL
    return nxt, reward, done

# --- Q-learning agent ---
Q = np.zeros((ROWS, COLS, len(ACTIONS)))

def choose_action(state, eps):
    if random.random() < eps:
        return random.randrange(len(ACTIONS))
    r, c = state
    return int(np.argmax(Q[r, c]))

def train(episodes=2000, alpha=0.2, gamma=0.95, eps_start=1.0, eps_min=0.05):
    eps = eps_start
    for ep in range(episodes):
        state = START
        for _ in range(200):
            a = choose_action(state, eps)
            nxt, r, done = step(state, a)
            sr, sc = state
            nr, nc = nxt
            best_next = np.max(Q[nr, nc])
            Q[sr, sc, a] += alpha * (r + gamma * best_next - Q[sr, sc, a])
            state = nxt
            if done:
                break
        eps = max(eps_min, eps * 0.995)

train()

# --- Run learned policy ---
state = START
path = [state]
for _ in range(50):
    a = int(np.argmax(Q[state[0], state[1]]))
    state, r, done = step(state, a)
    path.append(state)
    if done:
        break

print(f"Robot reached goal in {len(path)-1} steps" if state == GOAL else "Did not reach goal")
print("Path:", path)