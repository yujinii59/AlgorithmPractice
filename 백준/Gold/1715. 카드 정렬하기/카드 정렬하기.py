from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heappush(q, int(input()))
    
cnt = 0
while len(q) > 1:
    f, s = heappop(q), heappop(q)
    cnt += f + s
    heappush(q, f+s)
    
print(cnt)