while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    sanggun = {int(input()):1 for _ in range(n)}
    print(sum(sanggun.get(int(input()),0) for _ in range(m)))