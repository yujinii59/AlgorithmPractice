from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split())
known = deque(list(map(int, sys.stdin.readline().split()))[1:])
truth = [0]*(n+1)
for k in known:
    truth[k] = 1
members = {i+1:[] for i in range(n)}
parties = {}
for j in range(m):
    member = list(map(int, sys.stdin.readline().split()))[1:]
    parties[j] = member
    for mem in member:
        members[mem].append(j)
    
poss_party = [1]*m
while known:
    p = known.popleft()
    for party in members[p]:
        if poss_party[party] == 1:
            poss_party[party] = 0
            for mem in parties[party]:
                if truth[mem] == 0:
                    truth[mem] = 1
                    known.append(mem)
                    
print(sum(poss_party))