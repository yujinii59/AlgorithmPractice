a, p = map(int, input().split())
nums = {a:0}
i = 1
while True:
    num = 0
    for n in str(a):
        num += int(n)**p
    
    if num in nums:
        print(nums[num])
        break
    else:
        nums[num] = i
    a = num
    i+=1