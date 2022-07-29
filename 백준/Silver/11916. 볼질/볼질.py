def moves():
    for i in range(3):
        if grounds[i+1] > 1:
            grounds[i+1] -= 1
            grounds[i+2] += 1
        else:
            break

n = int(input())
balls = list(map(int, input().split()))
grounds = {i+1:0 for i in range(4)}
cnt = 0
for ball in balls:
    if ball == 1:
        cnt += 1
    elif ball == 2:
        cnt = 0
        grounds[1] += 1
        moves()
        
    elif ball == 3:
        cnt += 1
        for i in range(3, 0, -1):
            if grounds[i] > 0:
                grounds[i] -= 1
                grounds[i+1] += 1
    
    if cnt == 4:
        cnt = 0
        grounds[1] += 1
        moves()
    
        
print(grounds[4])
    
        