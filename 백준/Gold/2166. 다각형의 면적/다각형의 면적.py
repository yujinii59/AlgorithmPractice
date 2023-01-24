n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.append(points[0])
total = 0
for i in range(n):
    total += points[i][0] * points[i+1][1] - points[i][1] * points[i+1][0]
    
print(f'{abs(total)/2:.1f}')