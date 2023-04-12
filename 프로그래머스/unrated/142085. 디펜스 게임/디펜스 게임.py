import heapq

def solution(n, k, enemy):
    answer = 0
    pass_q = []
    fight = []
    total = 0
    count = 0
    for i, cnt in enumerate(enemy):
        heapq.heappush(pass_q, cnt)
        if i >= k:
            total += heapq.heappop(pass_q)
            count += 1
            
        if total > n:
            return count - 1 + k
            
    return len(enemy)