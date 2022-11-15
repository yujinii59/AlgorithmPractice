n = int(input())
win = ['CY','SK']

dp = [0]*(n+1)
for i in range(1, n+1):
    one, three, four = 0, 0, 0
    if i >= 1:
        one = dp[i-1]+1
    if i >= 3:
        three = dp[i-3]+1
    if i >= 4:
        four = dp[i-4]+1
        
    dp[i] = max(one % 2, three % 2, four % 2)
    
print(win[dp[n]])