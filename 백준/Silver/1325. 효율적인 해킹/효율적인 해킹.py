from collections import deque
import sys

n, m = map(int, input().split())
conn = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    conn[b].append(a)
    
q = deque()
hacking = {i:0 for i in range(1, n+1)}
for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    q.append(i)
    while q:
        comp = q.popleft()
        for c in conn[comp]:
            if visited[c] > 0:
                continue
            visited[c] = 1
            q.append(c)
    hacking[i] = sum(visited)
hacking = sorted(hacking.items(), key=lambda x:[-x[1], x[0]])
max_hacking = hacking[0][1]
for k, v in hacking:
    if v == max_hacking:
        print(k, end=' ')
    else:
        break