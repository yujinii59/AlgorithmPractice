def fibonacci(num):
    if num < 2:
        dp[num] = 1
    else:
        dp[num] = dp[num-1] + dp[num-2]

n = int(input())        
dp = [0 for _ in range(n+1)]
for i in range(n+1):
    fibonacci(i)
print(2 * (dp[n] + dp[n-1]))