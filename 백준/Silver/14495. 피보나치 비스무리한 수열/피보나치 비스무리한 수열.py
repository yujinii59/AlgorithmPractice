n = int(input())
dp = []
for i in range(n+1):
    if i <= 3:
        dp.append(1)
    else:
        dp.append(dp[i-1]+dp[i-3])
print(dp[n])