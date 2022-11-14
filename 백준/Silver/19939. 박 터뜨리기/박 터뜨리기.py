n, k = map(int, input().split())
res = n - (k * (k+1))/2
if res < 0:
    print(-1)
else:
    if res % k:
        print(k)
    else:
        print(k-1)