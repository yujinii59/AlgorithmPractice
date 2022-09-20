percentages = list(map(int, input().split()))
maps = [[1] * 8 for _ in range(8)]
loc = 0
for i in range(7):
    for j in range(i+1, 8):
        prcnt = percentages[loc]
        maps[i][j] = prcnt
        maps[j][i] = (100-prcnt)
        loc += 1
percents = [1] * 8
group = list(range(8))
for i in range(3):
    tmp = percents[:]
    for j,g in enumerate(group):
        q = g // 2
        r = (g+1) % 2
        group[j] = q
        start = (2**(i+1)) * q + (2**i) * r
        p = 0
        for k in range(2**i):
            p += percents[start+k] * maps[j][start+k]
        tmp[j] = p * percents[j] / 100
    percents = tmp
print(*percents)