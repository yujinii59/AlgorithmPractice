from collections import deque

n = int(input())
visited = [0] * n
jumps = list(map(int, input().split()))
loc = int(input()) - 1
q = deque()
q.append(loc)
visited[loc] = 1
while q:
    loc = q.popleft()
    jump = jumps[loc]
    if loc - jump >= 0:
        if visited[loc - jump] == 0:
            q.append(loc-jump)
            visited[loc-jump] = 1
    if loc + jump < n:
        if visited[loc+jump] == 0:
            q.append(loc+jump)
            visited[loc+jump] = 1
print(sum(visited))   