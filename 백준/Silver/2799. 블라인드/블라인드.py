m, n = map(int, input().split())
wndw = [input() for i in range(5*m+1)]

kinds = [0]*5
for i in range(m):
    for j in range(n):
        cnt = 0
        for k in range(4):
            if wndw[5*i+k+1][5*j+1] == '.':
                break
            cnt += 1
        kinds[cnt] += 1
print(*kinds)