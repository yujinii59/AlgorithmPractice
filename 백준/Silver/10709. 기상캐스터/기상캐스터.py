from collections import deque
h, w = map(int, input().split())
clouds = deque()
states = []
for i in range(h):
    states.append([-1] * w)
    state = input()
    for j in range(w):
        if state[j] == 'c':
            clouds.append((i, j, 0))
            states[i][j] = 0

while clouds:
    r, c, minute = clouds.popleft()
    if c + 1 < w and states[r][c+1] == -1:
        clouds.append((r, c+1, minute+1))
        states[r][c+1] = minute+1

for state in states:
    print(*state)