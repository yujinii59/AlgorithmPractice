n, m = map(int, input().split())
n1 = {alpha: i for i, alpha in enumerate(input()[::-1])}
n2 = {alpha: n+i for i, alpha in enumerate(input())}
t = int(input())

ants = ['']*(n+m)
for i, (ant, loc) in enumerate(n1.items()):
    curr = min(loc+max(0, t-(n-i-1)), m+i)
    ants[curr]=ant

for i, (ant, loc) in enumerate(n2.items()):
    curr = max(loc-max(0, t-i), i)
    ants[curr]=ant

print(*ants, sep='')