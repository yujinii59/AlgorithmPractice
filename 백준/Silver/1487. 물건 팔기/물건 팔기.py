n = int(input())
cust = sorted([list(map(int, input().split())) for _ in range(n)])
profit = 0
best_price = 0
for i, (price, _) in enumerate(cust):
    tmp = 0
    for want, deliver in cust[i:]:
        if price > deliver:
            tmp += price - deliver
    if tmp > profit:
        profit = tmp
        best_price = price
print(best_price)