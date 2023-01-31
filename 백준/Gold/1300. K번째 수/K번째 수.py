from sys import stdin


def count_below(number):
    count = 0
    for row in range(1, N+1):
        count += min((number-1) // row, N)
    return count


N = int(stdin.readline())
k = int(stdin.readline())

left, right = 0, N * N
while left <= right:
    middle = (left + right) // 2
    if count_below(middle) >= k:
        right = middle - 1
    else:
        left = middle + 1
print(right)