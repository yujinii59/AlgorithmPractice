from collections import deque

n = int(input())
cnt = 0
q = deque([n])
while q:
    h = q.popleft()
    if h == 1:
        continue
    if h % 2 == 0:
        cnt += (h // 2) ** 2
        q.append(h // 2)
        q.append(h // 2)
    else:
        cnt += (h // 2) * (h // 2 + 1)
        q.append(h // 2)
        q.append(h // 2 + 1)
print(cnt)