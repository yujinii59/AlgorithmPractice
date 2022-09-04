from itertools import permutations
n = int(input())
cases = permutations(list(range(1,n+1)), n)
for case in cases:
    print(*case)