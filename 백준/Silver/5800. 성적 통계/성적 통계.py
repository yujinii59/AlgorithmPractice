t = int(input())
for i in range(t):
    scores = sorted(list(map(int, input().split()))[1:], reverse=True)
    max_score, min_score, gap = scores[0], scores[0], 0
    prev = scores[0]
    for score in scores[1:]:
        max_score = max(score, max_score)
        min_score = min(score, min_score)
        gap = max(gap, prev-score)
        prev = score
    print(f'Class {i+1}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {gap}')