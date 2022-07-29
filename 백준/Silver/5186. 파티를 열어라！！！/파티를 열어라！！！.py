k = int(input())
for i in range(k):
    n, c, l = map(int, input().split())
    friends = {i+1:{'I':0, 'S':0} for i in range(l)}
    for _ in range(n):
        area, status = input().split()
        friends[int(area)][status] += 1
        
    cars = {i+1:[] for i in range(l)}
    for _ in range(c):
        area, limit = map(int, input().split())
        cars[area].append(limit)
        
    for area, limits in cars.items():
        limits = sorted(limits, reverse=True)
        for limit in limits:
            driver_cnt = friends[area]['S']
            drunken_cnt = friends[area]['I']
            if driver_cnt > 0:
                if drunken_cnt >= limit - 1:
                    friends[area]['I'] -= limit - 1
                    friends[area]['S'] -= 1
                    n -= limit
                else:
                    limit_tmp = limit - drunken_cnt
                    friends[area]['I'] = 0
                    n -= drunken_cnt
                    if driver_cnt >= limit_tmp:
                        friends[area]['S'] -= limit_tmp
                        n -= limit_tmp
                    else:
                        friends[area]['S'] = 0
                        n -= driver_cnt
    
    print(f'Data Set {i+1}:')
    print(n)