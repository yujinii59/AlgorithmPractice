from math import sqrt

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    diff = y-x
    n = int(sqrt(diff)) - 1
    cnts = []
    for i in range(3):
        if diff >= (n+i)*(n+i+1):
            tmp = diff-(n+i)*(n+i+1)
            if tmp <= n+i+1:
                cnts.append(2*(n+i) + 1)
            elif tmp <= 2 * (n+i+1):
                cnts.append(2*(n+i+1))
            
    print(min(cnts))