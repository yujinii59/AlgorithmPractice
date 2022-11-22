import sys

input = sys.stdin.readline


def dynamic(num):
    dp = [0, 0, 1]
    sum_dp = 1
    for i in range(num):
        case = sum_dp%1000000009
        sum_dp += case - dp[i]
        dp.append(case)
            
    return dp
        

n = int(input())
test_case = [int(input()) for _ in range(n)]
max_num = max(test_case)
dp = dynamic(max_num)
for num in test_case:
    print(dp[num+2])