nums = list(map(int, input().split()))
min_num = min(nums)
cnt = min_num
nums = [num-min_num for num in nums if num > min_num]
tmp = []
for i in range(len(nums)):
    q,r = divmod(nums[i], 3)
    cnt += q
    if r:
        tmp.append(r)
if set(tmp) == {1}:
    cnt += 1
elif len(tmp) >= 1:
    cnt += len(tmp)

print(cnt)