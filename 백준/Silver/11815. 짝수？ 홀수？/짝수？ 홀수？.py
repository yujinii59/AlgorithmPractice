from math import sqrt
n = int(input())
nums = list(map(int, input().split()))
for num in nums:
    if round(sqrt(num)) ** 2 == num:
        print(1, end=' ')
    else:
        print(0, end=' ')