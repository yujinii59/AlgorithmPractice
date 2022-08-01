def truck_move(curr, end, visited):
    visited[curr] = 1
    cycle = False
    if curr != end:
        for road in roads[curr]:
            visited_tmp = visited.copy()
            if cycle:
                break
            if visited_tmp[road] == 1:
                cycle = True
                break
            
            cycle = truck_move(road, end, visited_tmp)
            
    return cycle


n = int(input())
roads = {}
for i in range(n-1):
    m = int(input())
    if m == 0:
        roads[i+1] = list(input())
    else:
        roads[i+1] = list(map(int, input().split()))

visited = [0] * (n+1)
cycle = truck_move(1, n, visited)

if cycle:
    print('CYCLE')
else:
    print('NO CYCLE')