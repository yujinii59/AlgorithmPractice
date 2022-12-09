from collections import deque

n = int(input())
miro = list(map(int, input().split()))
visited = [0]*n
q = deque([(0, 0)])
visited[0] = 1
while q:
    cnt, num = q.popleft()
    if num == n-1:
        print(cnt)
        break
    for i in range(min(n-num-1,miro[num])):
        if miro[num+i+1] != 0 and visited[num+i+1] == 0:
            q.append((cnt+1, num+i+1))
            visited[num+i+1] = 1
else:
    print(-1)