import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    for num in list(map(int, input().split())):
        heapq.heappush(q, num)
        if len(q) > n:
            heapq.heappop(q)
        
print(heapq.nlargest(n, q)[n-1])