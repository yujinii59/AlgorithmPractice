n = int(input())
k = int(input())
known = {i: set() for i in range(1, n+1)}
for i in range(k):
    inp = list(map(int, input().split()))
    m = inp[0]
    p = inp[1:]
    if 1 in p:
        for j in p:
            known[j].add(i)
            
    else:
        total = set()
        for j in p:
            total = total | known[j]
        
        for j in p:
            tmp = total.copy()
            known[j] = tmp
            
print(1)
for j in range(2, n+1):
    if known[j] == known[1]:
        print(j)