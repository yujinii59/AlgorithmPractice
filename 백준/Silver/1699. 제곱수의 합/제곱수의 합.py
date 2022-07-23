def sum_of_square_numbers(num):
    min_cnt = [num]
    if num > 3:
        sqrt_of_num = int(num ** 0.5)
        while sqrt_of_num > 1:
            sq = sqrt_of_num ** 2
            if num // sq > 3:
                break
            min_cnt.append(1 + dp[num - sq])
            sqrt_of_num -= 1
    
    dp[num] = min(min_cnt)
    
    
n = int(input()) 
dp = [0 for _ in range(n+1)] 
for i in range(1,n+1):
    sum_of_square_numbers(i)
print(dp[n])