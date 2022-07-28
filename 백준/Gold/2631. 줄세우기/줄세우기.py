from collections import defaultdict
n = int(input())
dp = defaultdict(int)
max_len = 0
for _ in range(n):
    num = int(input())
    dp[num] = 1
    for k, v in dp.items():
        if k < num:
            dp[num] = max(dp[num], v+1)
            
    max_len = max(max_len, dp[num])
print(n - max_len)