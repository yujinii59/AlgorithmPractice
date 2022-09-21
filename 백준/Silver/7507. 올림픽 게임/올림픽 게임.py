import heapq
import sys

t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    games = []
    for _ in range(n):
        d, s, e = map(int, input().split())
        heapq.heappush(games, [d, e, s])

    cnt = 0
    prev_e = 0
    prev_d = 1
    while games:
        d, e, s = heapq.heappop(games)
        if d != prev_d:
            prev_e = 0
            prev_d = d

        if prev_e <= s:
            prev_e = e
            cnt += 1

    print(f'Scenario #{i + 1}:')
    print(cnt)
    print()