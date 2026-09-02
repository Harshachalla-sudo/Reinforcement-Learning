import numpy as np

# --- City grid: robot delivers from START to GOAL, cells have travel cost ---
# Higher cost = traffic/rough terrain; 'X' = impassable (blocked road)
GRID = [
    "1111111111",
    "1XX111111X",
    "1X311111X1",
    "1X1XXXXX11",
    "1X1X111111",
    "111X1XXXX1",
    "1XXX111111",
    "1111111111",
]
ROWS, COLS = len(GRID), len(GRID[0])
START = (0, 0)
GOAL = (7, 9)
MOVES = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

def is_free(pos):
    r, c = pos
    return 0 <= r < ROWS and 0 <= c < COLS and GRID[r][c] != 'X'

def move_cost(pos):
    r, c = pos
    return int(GRID[r][c])  # cost of entering that cell

INF = float('inf')

# --- Value Iteration: solve the Bellman optimality equation ---
V = np.full((ROWS, COLS), INF)
V[GOAL] = 0.0

def value_iteration(theta=1e-4, max_iters=1000):
    for it in range(max_iters):
        delta = 0.0
        new_V = V.copy()
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) == GOAL or not is_free((r, c)):
                    continue
                best = INF
                for dr, dc in MOVES:
                    nxt = (r+dr, c+dc)
                    if is_free(nxt):
                        candidate = move_cost(nxt) + V[nxt]
                        best = min(best, candidate)
                new_V[r, c] = best
                if best < INF:
                    delta = max(delta, abs(best - V[r, c]) if V[r, c] < INF else best)
        V[:] = new_V
        if delta < theta:
            print(f"Converged after {it+1} iterations")
            break

value_iteration()

# --- Extract optimal policy greedily from V* ---
def optimal_next(pos):
    best_move, best_val = None, INF
    for dr, dc in MOVES:
        nxt = (pos[0]+dr, pos[1]+dc)
        if is_free(nxt) and V[nxt] < INF:
            candidate = move_cost(nxt) + V[nxt]
            if candidate < best_val:
                best_val, best_move = candidate, nxt
    return best_move

# --- Trace the minimum-cost path from START to GOAL ---
path = [START]
pos = START
total_cost = 0
while pos != GOAL:
    nxt = optimal_next(pos)
    if nxt is None:
        print("No path found")
        break
    total_cost += move_cost(nxt)
    pos = nxt
    path.append(pos)

print(f"Optimal path ({len(path)-1} steps, total cost={total_cost}):")
print(path)
print(f"V*(start) = {V[START]}  (minimum cost-to-go from start)")
