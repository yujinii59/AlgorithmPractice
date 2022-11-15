n = int(input())
stocks = list(map(int, input().split()))
min_stock = stocks[0]
max_stock = stocks[0]
profit = 0
for stock in stocks:
    if min_stock > stock:
        min_stock = stock
        max_stock = stock
    elif max_stock < stock:
        max_stock = stock
        profit = max(profit, max_stock - min_stock)
print(profit)