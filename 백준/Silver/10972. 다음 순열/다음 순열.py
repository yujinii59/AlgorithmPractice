n = int(input())
nums = list(map(int, input().split()))
result = [-1]
for i in range(n-1, 0, -1):
    if nums[i] > nums[i-1]:
        chg = sorted(nums[i:])
        result = nums[:i-1]
        tmp = []
        k = 0
        for j in range(len(chg)):
            num = chg[j]
            if num > nums[i-1]:
                if k == 0:
                    k += 1
                    tmp.append(nums[i-1])
                    result.append(num)
                    result.extend(tmp + chg[j+1:])
                    break
            else:
                tmp.append(num)
        break
print(' '.join(list(map(str, result))))