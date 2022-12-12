from itertools import combinations
t = int(input())
for _ in range(t):
    n = int(input())
    ls = [input() for _ in range(n)]
    cases = combinations(ls, 2)
    for case in cases:
        s1 = case[0]+case[1]
        s2 = case[1]+case[0]
        if s1 == s1[::-1]:
            print(s1)
            break
        if s2 == s2[::-1]:
            print(s2)
            break
    else:
        print(0)