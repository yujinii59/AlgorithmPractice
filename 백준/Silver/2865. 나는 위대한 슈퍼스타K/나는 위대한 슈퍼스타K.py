n, m, k = map(int, input().split())
parti = {}
for _ in range(m):
    ab = list(map(float, input().split()))
    for i in range(n):
        score = parti.get(ab[2*i], 0)
        parti[ab[2*i]] = max(score, ab[2*i+1])
        
print(round(sum(sorted(parti.values(), reverse=True)[:k]), 1))