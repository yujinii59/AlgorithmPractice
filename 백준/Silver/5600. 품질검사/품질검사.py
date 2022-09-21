a, b, c = map(int, input().split())
t = int(input())
states = [2] * (a+b+c+1)
unknowns = []
for _ in range(t):
    i,j,k,r = map(int, input().split())
    if r:
        states[i] = 1
        states[j] = 1
        states[k] = 1
        
    else:
        unknowns.append([i,j,k])
        
for unknown in unknowns:
    u = []
    for p in unknown:
        if states[p] != 1:
            u.append(p)
    if len(u) == 1:
        states[u[0]] = 0
    
print(*states[1:], sep='\n')