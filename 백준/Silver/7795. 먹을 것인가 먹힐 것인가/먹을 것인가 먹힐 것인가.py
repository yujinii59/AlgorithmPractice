import sys

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = sorted(list(map(int, sys.stdin.readline().split())))
    b = sorted(list(map(int, sys.stdin.readline().split())))
    l = len(b)
    start = 0
    cnt = 0
    for num in a:
        cnt += start
        for j in range(start, l):
            if b[j] < num:
                cnt += 1
            else:
                start = j
                break
    print(cnt)