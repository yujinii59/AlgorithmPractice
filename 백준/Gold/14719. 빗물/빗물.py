h, w = map(int, input().split())
heights = list(map(int, input().split()))
comp = []
lefts = []
start = (0,heights[0])
end = heights[-1]
for i,height in enumerate(heights):
    if start[1] <= height:
        if start[0] + 1 < i:
            comp.append((start[0], i, start[1]))
        start = (i, height)
        lefts = []
    else:
        while lefts:
            loc, left = lefts.pop()
            if left > height:
                lefts.append((loc, left))
                break
            
    lefts.append((i, height))

for i in range(len(lefts)-1):
    if lefts[i][0] + 1 < lefts[i+1][0]:
        comp.append((lefts[i][0] + 1, lefts[i+1][0], lefts[i+1][1]))

total = 0
for s,e,height in comp:
    for i in range(s, e):
        total += height-heights[i]

print(total)