t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    strings = input().split()
    cases = {}
    for string in strings:
        upper_cnt = sum(s.isupper() for s in string)
        lower = ''.join(sorted(string.lower()))
        if (lower, upper_cnt) in cases:
            cases[(lower, upper_cnt)] += 1
        else:
            cases[(lower, upper_cnt)] = 1
    print(sum((cnt - 1) * cnt // 2 for cnt in cases.values() if cnt > 1))