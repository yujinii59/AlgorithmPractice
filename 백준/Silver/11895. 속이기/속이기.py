n = int(input())
nums = list(map(int, input().split()))
xor = nums[0]
min_num = nums[0]
for num in nums[1:]:
    min_num = min(min_num, num)
    xor = int(bin(xor ^ num), 2)
    

if xor == 0:
    print(sum(nums)-min_num)
else:
    print(0)