t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    cases = {m:1}
    cnt = 0
    for i, coin in enumerate(coins[::-1]):
        tmp = {}
        if i == n-1:
            for case, count in cases.items():
                if case % coin == 0:
                    cnt += count
        else:
            for case, count in cases.items():
                poss = case // coin
                for i in range(poss+1):
                    if tmp.get(case-coin*i, 0):
                        tmp[case-coin*i] += count
                    else:
                        tmp[case-coin*i] = count
            cases = tmp
    print(cnt)