n = int(input())
scores = [int(input()) for _ in range(n)]
reduce_score = 0
prev = scores[-1]+1
for score in scores[::-1]:
    if prev <= score:
        reduce_score += score-prev+1
        score = prev - 1
        
    prev = score
    
print(reduce_score)