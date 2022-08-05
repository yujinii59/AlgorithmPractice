from collections import deque

t = int(input())
q = deque()
for _ in range(t):
    a, b = map(int, input().split())
    q.append((a, b, 0))
    min_cnt = b-a
    while q:
        score, target, cnt = q.popleft()
        if score * 2 <= target + 3:
            q.append((score*2, target+3, cnt+1))
            q.append((score+1, target, cnt+1))
        else:
            min_cnt = min(min_cnt, cnt + (target - score))
    print(min_cnt)