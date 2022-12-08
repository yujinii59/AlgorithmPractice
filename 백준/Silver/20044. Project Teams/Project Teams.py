n = int(input())
avail = sorted(list(map(int, input().split())))
min_score = 2*avail[-1]
for i in range(n):
    min_score = min(min_score, avail[i]+avail[-(i+1)])
    
print(min_score)