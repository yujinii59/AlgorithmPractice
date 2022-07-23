moves = [(-2, 1), (-1, 2), (1, 2), (2, 1)]
n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    mv = (m-1) // 2 + 1
    if mv > 4:
        print(4)
    else:
        print(mv)
else:
    if m > 4:
        if m == 5:
            print(m - 1)
        else:
            print(m - 2)
    else:
        print(m)