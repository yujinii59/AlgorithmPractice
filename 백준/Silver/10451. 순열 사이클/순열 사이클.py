t = int(input())
for _ in range(t):
    n = int(input())
    seq = [0] + list(map(int, input().split()))
    cnt = 0
    visited = [0]*(n+1)
    for i in range(1, n+1):
        if visited[i] == 0:
            cnt += 1
            cycle = [i]
            while cycle:
                num = cycle.pop()
                if visited[num] == 0:
                    visited[num] = 1
                    cycle = [seq[num]]
                
    print(cnt)