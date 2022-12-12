from itertools import combinations

n, m = map(int, input().split())
rates = [list(map(int, input().split())) for _ in range(n)]
cases = list(combinations(list(range(m)), 3))
totals = {}
for i in range(n):
    for j, case in enumerate(cases):
        score = 0
        for num in case:
            score = max(score, rates[i][num])
        total = totals.get(j, 0)
        totals[j] = total+score
        
print(max(totals.values()))