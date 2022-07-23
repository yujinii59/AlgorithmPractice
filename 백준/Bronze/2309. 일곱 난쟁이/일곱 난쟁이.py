from itertools import combinations

heights = [int(input()) for _ in range(9)]
cases = combinations(heights, 7)
for case in cases:
    total = sum(case)
    if total == 100 and len(set(case)) == 7:
        case = sorted(case)
        print(*case, sep='\n')
        break