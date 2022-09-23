while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    diag = h ** 2 + w ** 2
    while True:
        b = False
        for i in range(1, int(int(diag / 2 + 1) ** 0.5 + 1)):
            res = (diag - i**2) ** 0.5
            if res == int(res) and i < res:
                if diag == h ** 2 + w ** 2:
                    if i > h:
                        b = True
                        print(i, int(res))
                        break
                else:
                    b = True
                    print(i, int(res))
                    break
        if b:
            break
            
        diag += 1