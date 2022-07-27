def decompose(number, int_cnt, dp):
    for i in range(number+1):
        if i == 0:
            dp[0] = [1] * int_cnt
        else:    
            for j in range(int_cnt):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum(dp[i-1][:j+1])
    return dp

n, k = map(int, input().split())
dp = [[0] * k for _ in range(n+1)]
dp = decompose(n, k, dp)
print(dp[n][k-1] % 1000000000)
