n = int(input())
price = [0] + list(map(int, input().split()))
dp = price.copy()
for i in range(1,n+1):
    cases = [price[i]]
    for j in range(1,i):
        cases.append(dp[i-j]+dp[j])
        
    dp[i] = min(cases)
print(dp[n])