from collections import deque
import sys

input = sys.stdin.readline

n, t, w = map(int, input().split())
res_time = {}
queue = deque()
for _ in range(n):
    p, time = map(int, input().split())
    res_time[p] = time
    queue.append(p)
    
m = int(input())
consumers={}
for _ in range(m):
    p, time, c = map(int, input().split())
    consumers[c] = [p, time]
    
i = 1
while i <= w:
    num = queue.popleft()
    spend = min(res_time[num], t, w-i+1)
    for j in range(spend):
        if consumers.get(i+j, 0):
            p, time = consumers[i+j]
            queue.append(p)
            res_time[p] = time
    res_time[num] -= spend
    i += spend
    if res_time[num]:
        queue.append(num)
        
    print(*([num]*spend), sep='\n')