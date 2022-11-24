from collections import Counter

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
counter = Counter(nums)
cnt = 0
for num in nums:
    if num == m-num:
        if counter[num] >= 2:
            cnt += 1
            counter[num]-=2
    else:
        if counter.get(num, 0) and counter.get(m-num, 0):
            cnt += 1
            counter[num]-=1
            counter[m-num]-=1
print(cnt)