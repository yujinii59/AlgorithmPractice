from sys import stdin
k = int(stdin.readline().strip())
for i in range(1, k+1):
    n, c, l = map(int, stdin.readline().strip().split())
    area = {}
    dType = {}
    yj = 0
    for _ in range(n):
        a, d = stdin.readline().strip().split()
        if a in area:
            area[a] += 1
            if d == 'S' and a in dType:
                dType[a] += 1
            elif d == 'S' and a not in dType:
                dType[a] = 1
        else:
            area[a] = 1
            if d == 'S':
                dType[a] = 1
    
    cars = {}
    for _ in range(c):
        b, p = stdin.readline().strip().split()
        if b in cars:
            cars[b].append(int(p))
        else:
            cars[b] = [int(p)]
            
            
    for b, cnt in cars.items():
        cnt = sorted(cnt, reverse=True)
        for c in cnt:
            if dType.get(b, 0):
                dType[b] -= 1
                area[b] -= c
                if area[b] <= 0:
                    area[b] = 0
                    dType[b] = 0
                    
    yj = sum(area.values())
    print(f"Data Set {i}:\n{yj}")
