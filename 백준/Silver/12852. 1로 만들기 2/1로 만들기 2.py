n = int(input())
dp = [0]*(n+1)
route = [[]]*(n+1)
route[1] = [1]
min_route = 0
for i in range(2, n+1):
    if i <= 3:
        dp[i] = 1
        route[i] = [i, 1]
    else:
        dp[i] = dp[i-1]+1
        min_route = i-1
        if i % 2 == 0:
            if dp[i] > dp[i//2]+1:
                dp[i] = dp[i//2]+1
                min_route = i//2
        if i % 3 == 0:
            if dp[i] > dp[i//3]+1:
                dp[i] = dp[i//3]+1
                min_route = i//3
        route[i] = [i] + route[min_route]
        
print(dp[n])
print(*route[n])