n, x = map(int, input().split())
visitors = list(map(int, input().split()))
max_visit = sum(visitors[:x])
cnt = 1
sum_visit = sum(visitors[:x])
for i, visitor in enumerate(visitors[x:]):
    sum_visit += visitor - visitors[i]
    if sum_visit > max_visit:
        max_visit = sum_visit
        cnt = 1
    elif sum_visit == max_visit:
        cnt += 1
        
if max_visit:
    print(max_visit)
    print(cnt)
else:
    print('SAD')