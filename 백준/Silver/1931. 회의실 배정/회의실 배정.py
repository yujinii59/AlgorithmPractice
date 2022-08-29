import heapq
n = int(input())
q = []
for _ in range(n):
    s,e = map(int, input().split())
    heapq.heappush(q, (e, s))
    
cnt = 0
end = 0
while q:
    e, s = heapq.heappop(q)
    if end <= s:
        cnt += 1
        end = e
print(cnt)