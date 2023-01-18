def check_square(x, y, points):
    coords = [(0,0), (0,1),(1,0),(1,1)]
    for a, b in coords:
        if (a+x, b+y) not in points:
            return False
    
    return True

n = int(input())
direction = {0:(1, 0), 1:(0, -1), 2:(-1, 0), 3:(0, 1)}
square = 0
total_point = set()
for _ in range(n):
    points = []
    x, y, d, g = map(int, input().split())
    points.append((x, y))
    dx, dy = direction[d]
    cx, cy = x+dx, y+dy
    points.append((cx, cy))
#     print('end',cx, cy)
    for _ in range(g):
        for i in range(len(points)-1, -1, -1):
            point = points[i]
            if point != (cx, cy):
                a, b = point
                a -= cx
                b -= cy
                a, b = -b, a
                a += cx
                b += cy
                points.append((a, b))
#                 print(a, b)
        cx, cy = a, b
#         print('end', cx, cy)
    total_point = total_point | set(points)
        

if len(total_point) >= 4:
    for a, b in total_point:
        if check_square(a, b, total_point):
            square += 1
print(square)