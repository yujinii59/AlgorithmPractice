n = int(input())
m = int(input())
locations = list(map(int, input().split()))
min_height = locations[0]
prev = 0
for loc in locations:
    height = (loc - prev) // 2
    if (loc - prev) % 2 == 1:
        height += 1
    min_height = max(min_height, height)
    prev = loc
    
if prev+min_height < n:
    min_height = n-prev

print(min_height)