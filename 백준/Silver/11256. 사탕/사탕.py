from functools import reduce

t = int(input())
for _ in range(t):
    j, n = map(int, input().split())
    sizes = [reduce(lambda x, y: x*y, list(map(int, input().split()))) for _ in range(n)]
    sizes = sorted(sizes, reverse=True)
    cnt = 0
    for size in sizes:
        if j > size:
            j -= size
            cnt += 1
        elif 0 < j <= size:
            j = 0
            cnt += 1
        else:
            break
    
    print(cnt)    