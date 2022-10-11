from collections import Counter

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    infos = []
    for _ in range(n):
        kinds = list(map(int, input().split()))
        num, kinds, money = kinds[0], Counter(kinds[1:-1]), kinds[-1]
        infos.append((money, num, kinds))
    infos = sorted(infos, key=lambda x: [-x[0], x[1], x[2]])
    stickers = [0] + list(map(int, input().split()))
    M = max(stickers)
    prize = 0
    for info in infos:
        money, num, kinds = info
        min_cnt = M
        for kind, cnt in kinds.items():
            min_cnt = min(min_cnt, stickers[kind]//cnt)
        
        for kind, cnt in kinds.items():
            stickers[kind] -= cnt * min_cnt
        
        prize += min_cnt * money
        
    print(prize)
            