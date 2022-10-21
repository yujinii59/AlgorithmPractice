from collections import deque

n = int(input())
tree = {i+1: [] for i in range(n)}
for _ in range(n-1):
    a, b, l = map(int, input().split())
    tree[a].append((b, l))
    tree[b].append((a, l))

q = deque([(1, 0, 0)])
max_len = 0
node = 1
while q:
    curr, prev, length = q.popleft()
    if max_len < length:
        max_len = length
        node = curr
        
    for nd, l in tree[curr]:
        if nd == prev:
            continue
            
        else:
            q.append((nd, curr, length+l))

q = deque([(node, 0, 0)])
max_len = 0
while q:
    curr, prev, length = q.popleft()
    if max_len < length:
        max_len = length
        
    for nd, l in tree[curr]:
        if nd == prev:
            continue
            
        else:
            q.append((nd, curr, length+l))
print(max_len)