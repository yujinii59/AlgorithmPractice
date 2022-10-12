from collections import deque

n = int(input())
m = int(input())
rel = {i+1:[] for i in range(n)}
for _ in range(m):
    a,b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

q = deque([(1, 0)])
visited = [0] * (n+1)
visited[1] = 1
while q:
    num, cnt = q.popleft()
    if cnt < 2:
        for r in rel[num]:
            if visited[r] == 0:
                q.append((r, cnt+1))
                visited[r] = 1
print(sum(visited)-1)