def handshake(num, dp):
    if num == 1:
        dp[1] = 1
    else:
        dp = [dp[1], (dp[0] + dp[1]) % 10]
    
    return dp

n = int(input()) % 60
dp = [1, 1]
for i in range(1, n+1):
    dp = handshake(i, dp)
    
print(dp[1])