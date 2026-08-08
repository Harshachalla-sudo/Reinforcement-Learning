import random
from collections import deque

N = 4  # board size

def king_moves(p):
    r, c = p
    return [(r+dr, c+dc) for dr in (-1,0,1) for dc in (-1,0,1)
            if (dr or dc) and 0<=r+dr<N and 0<=c+dc<N]

def rook_moves(p, blockers):
    r, c = p
    out = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        while 0<=nr<N and 0<=nc<N and (nr,nc) not in blockers:
            out.append((nr,nc)); nr+=dr; nc+=dc
    return out

def adj(a, b):
    return max(abs(a[0]-b[0]), abs(a[1]-b[1])) <= 1

# state = (white_king, white_rook, black_king); reward: +100 mate, -1 per move
def legal_actions(s):
    wk, wr, bk = s
    acts = [('K',t) for t in king_moves(wk) if t!=wr and not adj(t,bk)]
    acts += [('R',t) for t in rook_moves(wr, {wk,bk})]
    return acts

def black_replies(wk, wr, bk):
    zone = set(king_moves(wk)) | {wk}
    line = set(rook_moves(wr, {wk}))
    return [t for t in king_moves(bk)
            if t!=wk and t not in zone
            and (t!=wr or wr not in zone)
            and (t==wr or t not in line)]

def step(s, a):
    wk, wr, bk = s
    wk, wr = (a[1], wr) if a[0]=='K' else (wk, a[1])
    replies = black_replies(wk, wr, bk)
    if not replies:
        checkmate = bk in set(rook_moves(wr, {wk}))
        return [((wk,wr,bk), 1.0, 100 if checkmate else -20, True)]
    p = 1/len(replies)
    return [((wk,wr,bk2), p, -1, False) for bk2 in replies]

def sample_step(s, a):
    outs = step(s, a)
    states, probs, rewards, dones = zip(*outs)
    i = random.choices(range(len(outs)), weights=probs)[0]
    return states[i], rewards[i], dones[i]

# --- Q-learning ---
Q = {}
def best(s, actions):
    return max(actions, key=lambda a: Q.get((s,a), 0.0))

def train(start, episodes=4000, alpha=0.3, gamma=0.95, eps=1.0):
    for ep in range(episodes):
        eps = max(0.05, eps*0.999)
        s = start
        for _ in range(30):
            acts = legal_actions(s)
            a = random.choice(acts) if random.random()<eps else best(s, acts)
            s2, r, done = sample_step(s, a)
            future = 0 if done else Q.get((s2, best(s2, legal_actions(s2))), 0.0)
            Q[(s,a)] = Q.get((s,a),0.0) + alpha*(r + gamma*future - Q.get((s,a),0.0))
            if done: break
            s = s2

start = ((0,0), (0,3), (2,2))
train(start)

# play out learned policy
s = start
for i in range(15):
    acts = legal_actions(s)
    a = best(s, acts)
    s, r, done = sample_step(s, a)
    print(f"move {i+1}: {a}, reward={r}")
    if done:
        print("checkmate!" if r == 100 else "draw")
        break