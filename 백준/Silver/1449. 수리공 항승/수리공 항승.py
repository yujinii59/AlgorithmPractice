n, l = map(int, input().split())
locations = sorted(list(map(int, input().split())))
start = -1
end = -1
cnt = 0
for loc in locations:
    if end < loc + 0.5:
        cnt += 1
        if end <= loc - 0.5:
            start = loc - 0.5
        else:
            start = end
        end = start + l
print(cnt)
    