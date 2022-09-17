from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())
lamps = [sys.stdin.readline().split()[1:] for _ in range(n)]
cases = combinations(lamps, n-1)
poss = False
for case in cases:
    sets = set(sum(case,[]))
    if len(sets) == m:
        poss = True
        break
if poss:
    print(1)
else:
    print(0)