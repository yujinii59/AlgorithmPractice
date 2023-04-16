from collections import deque

def solution(storey):
    answer = storey
    storeies = deque([(storey, 0)])
    while storeies:
        storey, cnt = storeies.popleft()
        if storey == 0:
            answer = min(answer, cnt)
            
        else:
            storey, r = divmod(storey, 10)
            if r <= 5:
                storeies.append((storey, cnt+r))
            if r >= 5:
                storeies.append((storey+1, cnt+10-r))
    
    return answer