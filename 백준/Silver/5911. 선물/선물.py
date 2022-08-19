import heapq
n, money = map(int, input().split())
gifts = []
for _ in range(n):
    p, s = map(int, input().split())
    heapq.heappush(gifts, (p+s, s, p))
    
cnt = 0
max_price = 0
for _ in range(n):
    price, s, p = heapq.heappop(gifts)
    max_price = max(max_price, p)
    if money < price:
        money += max_price / 2
        if money >= price:
            cnt += 1
            money -= price
        break
    elif money >= price:
        cnt += 1
        money -= price
print(cnt)