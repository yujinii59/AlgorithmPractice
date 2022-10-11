t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    money = [0] + list(map(int, input().split()))
    if n == m:
        if sum(money) < k:
            cnt = 1
        else:
            cnt = 0
    else:
        money.extend(money[1:m])
        steal = sum(money[:m])
        cnt = 0
        for i in range(n):
            steal = steal - money[i] + money[m+i]
            if steal < k:
                cnt += 1
            
    print(cnt)