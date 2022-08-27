t = int(input())
for _ in range(t):
    n = int(input())
    first = {s: i for i, s in enumerate(input().split())}
    second = [first[s] for s in input().split()]
    rst = [''] * n
    for i, s in enumerate(input().split()):
        rst[second[i]] = s
        
    print(*rst)