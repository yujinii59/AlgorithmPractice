t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    vel = list(map(int, input().split()))
    min_time = x
    for v in vel[:-1]:
        min_time = min(x / v, min_time)
    
    v = vel[-1]
    dist = v * min_time
    if dist >= x:
        print(0)
    else:
        x -= dist - v
        if x >= y:
            print(-1)
        else:
            print(int(x+1))