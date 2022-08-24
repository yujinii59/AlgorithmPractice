n, k = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(n)]
scores = sorted(scores, key=lambda x: [-x[1], -x[2], -x[3], x[0]])
prev = [-1,-1,-1]
rank = 0
for i, score in enumerate(scores):
    if prev != score[1:]:
        rank = i+1
        prev = score[1:]
    
    if score[0] == k:
        break
    
    
print(rank)