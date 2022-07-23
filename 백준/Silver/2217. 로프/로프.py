n = int(input())
rope = sorted([int(input()) for _ in range(n)])
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, (n-i) * rope[i])
print(max_weight)