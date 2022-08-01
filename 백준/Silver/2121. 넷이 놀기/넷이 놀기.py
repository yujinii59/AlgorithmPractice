n = int(input())
points = set()
width, depth = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))
    

cnt = 0
for p_x, p_y in points:
    intersect = set([(p_x + width, p_y),(p_x, p_y + depth),(p_x + width, p_y + depth)]) & points
    if len(intersect) == 3:
        cnt += 1

print(cnt)