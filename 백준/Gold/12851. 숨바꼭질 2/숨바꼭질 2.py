from collections import deque

n, k = map(int, input().split())
q = deque([(n, 0)])
min_move = abs(n-k)
visited = set()
cnt = 0
while q:
    loc, move = q.popleft()
    visited.add(loc)
    if min_move < move:
        break
        
    if loc == k:
        if min_move > move:
            min_move = move
            cnt = 1
        elif min_move == move:
            cnt += 1
    
    else:
        if loc < k:
            if loc+1 not in visited and loc+1 <= 100000:
                q.append((loc+1, move+1))
            
            if loc*2 not in visited and loc*2 <= 100000:
                q.append((loc*2, move+1))
                
        if loc-1 not in visited and loc-1 >= 0:
            q.append((loc-1, move+1))
        
print(min_move)
print(cnt)