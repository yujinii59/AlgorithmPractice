from collections import deque

n, m = map(int, input().split())
ladders = {}
for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b

snakes = {}
for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b

q = deque()
q.append((1, 0))
min_cnt = 100
while q:
    loc, cnt = q.popleft()
    if loc >= 100:
        min_cnt = min(min_cnt, cnt)
        break

    j = 0
    for i in range(6):
        location = loc + i + 1
        move = ladders.get(location, location)
        move = snakes.get(location, move)
        if location != move:
            q.append((move, cnt + 1))
        elif location == move:
            j = location
    if j:
        q.append((j, cnt + 1))
print(min_cnt)