from collections import deque
import sys

t = int(input())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    times = list(map(int, sys.stdin.readline().split()))
    prev_cnt = [0]*n
    conn = {i:[] for i in range(n)}
    prev = {i:[] for i in range(n)}
    poss = set(list(range(n)))
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        prev_cnt[y-1] += 1
        conn[x-1].append(y-1)
        prev[y-1].append(x-1)
        poss.discard(y-1)

    num = int(input())

    poss = deque(list(poss))
    rst = [0] * n
    while poss:
        building = poss.popleft()
        time = 0
        for b in prev[building]:
            time = max(time, rst[b])
        rst[building] = time + times[building]
        if building == num-1:
            print(rst[building])
            break

        for b in conn[building]:
            prev_cnt[b] -= 1
            if prev_cnt[b] == 0:
                poss.append(b)
