from collections import deque

n = int(input())
card = deque([i for i in range(1, n+1)])
arr = []

while len(card)>0:
    arr.append(card.popleft())
    if card:
        card.append(card.popleft())
print(*arr)