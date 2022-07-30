from functools import reduce
from itertools import combinations_with_replacement

def check(n, a):
    for comb in combinations_with_replacement(range(1, 10), n):
        mutiple = reduce(lambda x, y: x * y, comb)
        if mutiple > a:
            return comb

    return [-1]

n = int(input())
a = list(map(int, input().split()))
a_multiple = reduce(lambda x, y: x * y, a)

print(*check(n, a_multiple))