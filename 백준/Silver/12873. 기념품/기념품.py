from collections import deque

n = int(input())
q = deque(list(range(1, n+1)))
for i in range(n-1):
    q.rotate(-((i+1)**3 - 1))
    q.popleft()
    
print(q.popleft())