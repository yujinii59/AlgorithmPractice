from collections import deque

n, k = map(int, input().split())
cnt = n * k
q = deque()
for i in range(n):
    cards = list(map(int, input().split()))
    for card in cards:
        q.append((i+1, card))
        
for _ in range(n*k - 1):
    p, card = q.popleft()
    cnt -= 1
    card %= cnt
    q.rotate(-(card-1))
    
print(*q.popleft())