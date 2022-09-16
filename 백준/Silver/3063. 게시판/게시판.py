t = int(input())
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    size = (x2-x1) * (y2-y1)
    if x1 < x4 and x2 > x3 and y1 < y4 and y2 > y3:
        size -= (min(x2, x4) - max(x1, x3)) * (min(y2, y4) - max(y1, y3))
        
    print(size)