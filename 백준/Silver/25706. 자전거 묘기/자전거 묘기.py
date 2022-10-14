n = int(input())
roads = list(map(int, input().split()))

dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    road = roads[i]
    dp[i] = dp[min(n, i+1+road)]+1
    
print(*dp[:-1])