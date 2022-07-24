n, m = map(int, input().split())
start = 1
end = m
j = int(input())
dist = 0
for _ in range(j):
    apple = int(input())
    if apple < start:
        d = start - apple
        dist += d
        end -= d
        start -= d
    elif apple > end:
        d = apple - end
        dist += d
        end += d
        start += d
        
print(dist)