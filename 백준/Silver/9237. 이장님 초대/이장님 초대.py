import heapq

n = int(input())
trees = list(map(int, input().split()))
q = []
for tree in trees:
    heapq.heappush(q, (-tree))
    
days = 1
max_day = 1
while q:
    days += 1
    tree = heapq.heappop(q)
    max_day = max(max_day, days-tree)
    
print(max_day)