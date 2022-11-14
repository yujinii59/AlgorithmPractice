n, m = map(int, input().split())
cost = 0
need = []
for _ in range(m):
    a, b = map(int, input().split())
    if a < n:
        need.append(n-a)
        
need = sorted(need)
if need:
    cost = sum(need[:-1])
print(cost)