n = int(input())
balloons = [(idx+1, b) for idx, b in enumerate(list(map(int, input().split())))]
i = 0
while balloons:
    l = len(balloons)
    if abs(i) >= l:
        if i < 0:
            i = -(abs(i) % l)
        else:
            i = i % l
    idx, b = balloons.pop(i)
    print(idx, end=' ')
    if i >= 0:
        if b > 0:
            i += b - 1
        else:
            i += b
    else:
        if b < 0:
            i += b + 1
        else:
            i += b
    