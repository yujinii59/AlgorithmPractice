n = int(input())
m, k = map(int, input().split())
pens = sorted(map(int, input().split()), reverse=True)
res = m*k
cnt = 0
for pen in pens:
    res -= pen
    cnt += 1
    if res <= 0:
        print(cnt)
        break
else:
    print('STRESS')