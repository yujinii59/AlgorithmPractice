while True:
    n = int(input())
    if n == 0:
        break
    stations = sorted([int(input()) for _ in range(n)] + [1422])
    if stations[0] > 0:
        print('IMPOSSIBLE')
    else:
        prev = stations[0]
        gap = 0
        poss = True
        for i, station in enumerate(stations[1:]):
            gap = station - prev
            if i < n-1:
                if gap > 200:
                    poss = False
                    break
            else:
                if gap > 100:
                    poss = False
                    break
            prev = station

        if poss:
            print('POSSIBLE')
        else:
            print('IMPOSSIBLE')