n, m = map(int, input().split())
payments = [0]+list(map(int, input().split()))
max_profit = 0
profit = sum(payments[:m])
for i in range(n-m+1):
    profit += payments[i+m]-payments[i]
    max_profit = max(max_profit, profit)
    
print(max_profit)