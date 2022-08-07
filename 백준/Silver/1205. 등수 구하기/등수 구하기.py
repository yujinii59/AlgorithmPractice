n, ts, p = map(int, input().split())
if n == 0:
    print(1)
else:
    data = list(map(int, input().split()))
    data.append(ts)
    data.sort(reverse=True)
    
    idx = data.index(ts)
    if n < p:
        print(idx + 1)
    else:
        if idx < p:
            if data[-1] == ts:
                print(-1)
            else:
                print(idx+1)
        else:
            print(-1)