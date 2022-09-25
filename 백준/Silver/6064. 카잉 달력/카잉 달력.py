from math import gcd
import sys

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    lcm =  m * n // gcd(m, n)
    rst = -1
    if n <= m:
        for i in range(lcm // m):
            year = m * i + x
            if (year-y) % n == 0:
                rst = year
                break
    else:
        for i in range(lcm // n):
            year = n * i + y
            if (year-x) % m == 0:
                rst = year
                break
    print(rst)