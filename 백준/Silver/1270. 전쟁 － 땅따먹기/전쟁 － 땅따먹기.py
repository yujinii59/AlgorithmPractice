from collections import Counter

n = int(input())
for _ in range(n):
    states = list(map(int, input().split()))
    half = states[0] / 2
    states = Counter(states[1:])
    rst = 'SYJKGW'
    for num, cnt in states.items():
        if cnt > half:
            rst = num
            break
    print(rst)