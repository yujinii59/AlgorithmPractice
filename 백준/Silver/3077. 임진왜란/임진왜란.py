from itertools import combinations
n = int(input())
ans = {war:i for i, war in enumerate(input().split())}
cases = combinations(input().split(), 2)
cnt = 0
total = 0
for case in cases:
    w1, w2 = case
    total += 1
    if ans[w1] < ans[w2]:
        cnt += 1
        
print(f'{cnt}/{total}')