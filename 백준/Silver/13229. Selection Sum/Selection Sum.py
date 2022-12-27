n = int(input())
nums = list(map(int, input().split()))
sum_nums = [nums[0]]
for i in range(n-1):
    sum_nums.append(sum_nums[i] + nums[i+1])
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    if s:
        print(sum_nums[e]-sum_nums[s-1])
    else:
        print(sum_nums[e])