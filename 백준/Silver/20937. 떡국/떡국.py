n = int(input())
sizes = list(map(int, input().split()))
bowls = {}
for size in sizes:
    if bowls.get(size, 0):
        bowls[size] += 1
    else:
        bowls[size] = 1
print(max(bowls.values()))