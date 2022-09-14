n, a, d = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if num == a:
        a += d
        cnt += 1
print(cnt)