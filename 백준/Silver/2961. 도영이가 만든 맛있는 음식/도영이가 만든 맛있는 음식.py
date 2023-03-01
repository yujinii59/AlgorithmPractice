n = int(input())
min_diff = int(1e10)
cases = []
for _ in range(n):
    s, b = map(int, input().split())
    min_diff = min(abs(s-b), min_diff)
    tmp = [(s, b)]
    for case in cases:
        sour, bitter = case
        sour *= s
        bitter += b
        min_diff = min(abs(sour-bitter), min_diff)
        tmp.append((sour, bitter))
    cases.extend(tmp)

print(min_diff)