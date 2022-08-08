n = int(input())
stairs = [[0, 0] for _ in range(n)]
scores = []
for _ in range(n):
    scores.append(int(input()))
    
for i in range(n):
    if i == 0:
        stairs[i][0] = scores[i]
    elif i == 1:
        stairs[i][0] = stairs[i-1][0] + scores[i]
        stairs[i][1] = scores[i]
    else:
        stairs[i][0] = stairs[i-1][1] + scores[i]
        stairs[i][1] = max(stairs[i-2]) + scores[i]
        
print(max(stairs[n - 1]))