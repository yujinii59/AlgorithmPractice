t = int(input())
for _ in range(t):
    n = int(input())
    scores = []
    for _ in range(2):
        scores.append(list(map(int, input().split())))
    
    score = [0,0]
    for i in range(n):
        score[0], score[1] = max(score[0], score[1] + scores[0][i]), max(score[1], score[0] + scores[1][i])
    
    print(max(score))