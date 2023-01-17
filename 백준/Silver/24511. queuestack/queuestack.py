from collections import deque

n = int(input())
kind = list(map(int, input().split()))
queue = deque()
elems = list(map(int, input().split()))
for i in range(n):
    if kind[i] == 0:
        queue.appendleft(elems[i])
        
m = int(input())
for elem in list(map(int, input().split())):
    queue.append(elem)
    print(queue.popleft(), end=' ')