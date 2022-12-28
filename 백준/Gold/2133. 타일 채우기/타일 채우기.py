n = int(input())
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    if i % 2 == 0:
        for j in range(i//2):
            if j == 0:
                dp[i] = dp[i-2]*3
            else:
                dp[i] += dp[i-2*(j+1)]*2
print(dp[n])