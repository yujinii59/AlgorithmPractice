def make_password(kinds):
    cnt = 0
    for res in kinds:
        if res <= 0:
            cnt += 1
    if cnt == 4:
        return 1
    else:
        return 0

idxes = {'A':0, 'C':1,'G':2,'T':3}
s, p = map(int, input().split())
string = input()
kinds = list(map(int, input().split()))
count = 0
for ss in string[:p]:
    kinds[idxes[ss]] -= 1

count += make_password(kinds)
        
idx = 0
for i in range(p, s):
    kinds[idxes[string[idx]]] += 1
    kinds[idxes[string[i]]] -= 1
    count += make_password(kinds)
    idx += 1
    
print(count)