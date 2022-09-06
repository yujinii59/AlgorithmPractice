def dfs(num, p, q, dp):
    if not dp.get(num, 0):
        dp[num] = dfs(num//p, p, q, dp) + dfs(num//q, p, q, dp)
    return dp[num]

n, p, q = map(int, input().split())
dp = {0:1}
dp[n] = dfs(n, p, q, dp)
print(dp[n])