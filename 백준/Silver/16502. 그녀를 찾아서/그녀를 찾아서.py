t = int(input())
m = int(input())
perc = {'A': 1, 'B': 1, 'C': 1, 'D': 1}
conn = {'A': [], 'B': [], 'C': [], 'D': []}
for _ in range(m):
    a, b, p = input().split()
    p = float(p)
    conn[a].append((b, p))
    
for _ in range(t):
    tmp = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for loc in ['A','B','C','D']:
        for store, p in conn[loc]:
            tmp[store] += perc[loc] * p
            
    total = sum(list(tmp.values())) 
    for k, v in tmp.items():
        perc[k] = v / total
        
for v in perc.values():
    print(v * 100)