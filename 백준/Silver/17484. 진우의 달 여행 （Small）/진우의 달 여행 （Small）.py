n, m = map(int, input().split())
fuels = [[1000]*3] + [[0]*3 for _ in range(m)] + [[1000]*3]
min_fuel = 1000
for _ in range(n):
    min_fuel = 1000
    fuel = list(map(int, input().split()))
    tmp = [[1000]*3] + [[] for _ in range(m)] + [[1000]*3]
    for i in range(m):
        tmp[i+1].append(min(fuels[i][1:])+fuel[i])
        tmp[i+1].append(min(fuels[i+1][0],fuels[i+1][2])+fuel[i])
        tmp[i+1].append(min(fuels[i+2][:2])+fuel[i])
        min_fuel = min(min_fuel, min(tmp[i+1]))
    fuels = tmp
print(min_fuel)