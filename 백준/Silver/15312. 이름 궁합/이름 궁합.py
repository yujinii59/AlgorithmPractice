from string import ascii_uppercase

alphabet = [3,2,1,2,3,3,2,3,3,2,2,1,2,2,1,2,2,2,1,2,1,1,1,2,2,1]
alphabet = {alpha: num for alpha, num in zip(ascii_uppercase, alphabet)}

name = input()
hname = input()
nums = []
for a,b in zip(name, hname):
    nums.append(alphabet[a])
    nums.append(alphabet[b])
    
while len(nums) > 2:
    tmp = []
    for i in range(len(nums)-1):
        tmp.append((nums[i] + nums[i+1]) % 10)
    nums = tmp

print(*tmp, sep='')