from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
cnt = 0
num = 0
queue = deque()
for _ in range(n):
    info = list(map(int, input().split()))
    if len(info) == 2:
        queue.append(info[1])
        count = len(queue)
        if count > cnt:
            num = info[1]
            cnt = count
        elif count == cnt and num > info[1]:
            num = info[1]
    else:
        queue.popleft()
print(cnt, num)