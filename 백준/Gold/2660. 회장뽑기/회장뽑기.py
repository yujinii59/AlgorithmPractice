n = int(input())
scores = [[n] * (n+1) for _ in range(n+1)]
for i in range(n):
    scores[i+1][i+1] = 0
    
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
        
    scores[a][b] = 1
    scores[b][a] = 1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        if scores[i][k] > 0:
            for j in range(i+1, n+1):
                if scores[k][j] > 0:
                    scores[i][j] = min(scores[i][j], scores[i][k] + scores[k][j])
                    scores[j][i] = scores[i][j]

score = sorted([(max(scores[i][1:]), i) for i in range(n+1)])
sc = score[0][0]
candidate = [score[i][1] for i in range(n+1) if score[i][0] == sc]
print(sc, len(candidate))
print(*candidate)