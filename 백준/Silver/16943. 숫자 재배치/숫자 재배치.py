from itertools import permutations

a, b = input().split()
if len(a) > len(b):
    print(-1)
else:
    b = int(b)
    max_val = ''.join(sorted(a, reverse=True))
    if int(max_val) < b:
        print(max_val)
    elif int(max_val[::-1]) >= b:
        print(-1)
    else:
        cases = set(permutations(a, len(a)))
        rst = -1
        for case in cases:
            if case[0] == '0':
                continue
            num = int(''.join(case))
            if num < b:
                if rst < num:
                    rst = num
        print(rst)