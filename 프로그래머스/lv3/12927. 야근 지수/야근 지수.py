import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    while n > 0 and works:
        n -= 1
        res = heapq.heappop(works)
        if res+1 < 0:
            heapq.heappush(works, res+1)
        
    answer = sum([x**2 for x in works])
    return answer