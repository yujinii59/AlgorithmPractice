from collections import deque

t = int(input())
q = deque()
for _ in range(t):
    v, e = map(int, input().split())
    conn = {}
    sep = []
    for i in range(v+1):
        conn[i] = []
        sep.append(0)
    
    for _ in range(e):
        a, b = map(int, input().split())
        conn[a].append(b)
        conn[b].append(a)
    
    bi_graph = True
    for i in range(1, v+1):
        if bi_graph:
            if sep[i] == 0:
                sep[i] = 1
                q.append((i, 1))
                while q:
                    p, s = q.popleft()
                    for point in conn[p]:
                        if sep[point] == s:
                            bi_graph = False
                            q.clear()
                            break
                        elif sep[point] == 0:
                            sep[point] = -s
                            q.append((point, -s))
    if bi_graph:
        print('YES')
    else:
        print('NO')