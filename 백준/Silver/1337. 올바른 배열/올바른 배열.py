n = int(input())
arr = sorted([int(input()) for _ in range(n)])
nums = set(arr)
min_cnt = 4
for num in arr:
    cnt = 5
    for i in range(5):
        if num+i in nums:
            cnt -= 1
    min_cnt = min(min_cnt, cnt)
print(min_cnt)