def investment(year, dp):
    profit = dp[year-1] * 1.05
    if year >= 3:
        profit = max(profit, dp[year-3] * 1.2)
        
    if year >= 5:
        profit = max(profit, dp[year-5] * 1.35)
        
    return int(profit)

money, y = map(int, input().split())
dp = [0] * (y+1)
dp[0] = money
for i in range(y):
    dp[i+1] = investment(i+1, dp)
    
print(dp[y])