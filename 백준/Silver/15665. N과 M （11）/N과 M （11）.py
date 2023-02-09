from itertools import product

n, m = map(int, input().split())
seq = sorted(list(set(map(int, input().split()))))
cases = product(seq, repeat=m)
for case in cases:
    print(*case, sep=' ')