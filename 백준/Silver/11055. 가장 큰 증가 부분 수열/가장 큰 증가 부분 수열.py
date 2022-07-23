n = int(input())
seq = list(map(int, input().split()))
dp = {}
max_val = 0
for i in seq:
    dp[i] = i
    for num in dp:
        if num < i:
            dp[i] = max(dp[i], dp[num] + i)
            
    max_val = max(max_val, dp[i])
print(max_val)