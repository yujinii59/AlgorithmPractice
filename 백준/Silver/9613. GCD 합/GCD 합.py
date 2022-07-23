from itertools import combinations
from math import gcd

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    n = nums[0]
    nums = nums[1:]
    cases = combinations(nums, 2)
    gcd_ls = list(gcd(c1, c2) for c1, c2 in cases)
    print(sum(gcd_ls))