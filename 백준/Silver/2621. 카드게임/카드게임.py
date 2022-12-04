colors = {}
nums = {}
for _ in range(5):
    color, num = input().split()
    num = int(num)
    colors[color] = colors.get(color, 0) + 1
    nums[num] = nums.get(num, 0) + 1
    
min_num = min(nums.keys())
max_num = max(nums.keys())
score = 100 + max_num
num_len = len(nums)
if len(colors) == 1:
    if num_len == 5 and max_num-min_num == 4:
        score = max(score, 900+max_num)
    else:
        score = max(score, 600+max_num)
        
if num_len == 5 and max_num-min_num == 4:
    score = max(score, 500+max_num)
    
if num_len == 2:
    tmp = 0
    for num, cnt in nums.items():
        if cnt == 4:
            tmp += 800 + num
        elif cnt == 3:
            tmp += 10 * num
        elif cnt == 2:
            tmp += num + 700
            
    score = max(score, tmp)
    
if num_len == 3:
    tmp = []
    for num, cnt in nums.items():
        if cnt == 3:
            score = max(score, 400+num)
        elif cnt == 2:
            tmp.append(num)
            
    if tmp:
        tmp = sorted(tmp)
        score = max(score, 10*tmp[1]+tmp[0]+300)
        
if num_len == 4:
    for num, cnt in nums.items():
        if cnt == 2:
            score = max(score, 200 + num)
            
print(score)