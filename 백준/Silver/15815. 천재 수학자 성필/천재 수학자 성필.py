def calc(nums, ops):
    length = len(ops)
    ans = nums.pop()
    for i in range(length):
        num = nums.pop()
        op = ops[i]
        ans = str(int(eval(num+op+ans)))
    nums.append(ans)
    return nums

seq = input()
nums = []
ops = []
prev = ''
for elem in seq:
    if elem.isdecimal():
        if prev == 'op':
            nums = calc(nums, ops)
            ops = []
        nums.append(elem)
        prev = 'num'
    else:
        ops.append(elem)
        prev = 'op'
nums = calc(nums, ops)
print(nums[0])