from itertools import permutations
n = input()
if n == ''.join(sorted(n, reverse=True)):
    print(0)
else:
    cases = permutations(n, len(n))
    num = int(n)
    min_num = 999999
    for case in cases:
        if int(''.join(case)) > num:
            min_num = min(min_num, int(''.join(case)))
    print(min_num)