n, k = map(int, input().split())
coins = sorted(list(set(int(input()) for _ in range(n))))
cnts = [0] * coins[0]
INF = int(1e6)
for i in range(coins[0],k+1):
    count = INF
    for coin in coins:
        if coin == i:
            count = 1
        elif coin < i:
            if cnts[i-coin]:
                count = min(count, cnts[i-coin] + 1)
        else:
            break
    
    if count == INF:
        count = 0
    cnts.append(count)
if cnts[k]:
    print(cnts[k])
else:
    print(-1)