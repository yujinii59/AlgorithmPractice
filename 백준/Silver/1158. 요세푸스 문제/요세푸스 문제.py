from collections import deque
n, k = map(int, input().split())
q = deque(list(map(str, range(1, n+1))))
i = 0
result = []
while q:
    i += 1
    p = q.popleft()
    if i < k:
        q.append(p)
    else:
        i = 0
        result.append(p)
        
print(f'<{", ".join(result)}>')