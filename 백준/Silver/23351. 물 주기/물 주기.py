n, k, a, b = map(int, input().split())
leaves = [k for _ in range(n)]
days = 0
i = 0
while True:
    if min(leaves) == 0:
        break
    days += 1
    for j in range(n):
        leaves[j] -= 1
        if 0 <= j-i < a:
            leaves[j] += b
    i = (i+a) % n
print(days)