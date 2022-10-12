n = int(input())
boxes = list(map(int, input().split()))
dp = {}
max_cnt = 1
for box in boxes:
    count = dp.get(box, 1)
    for size, cnt in dp.items():
        if size < box:
            count = max(count, cnt+1)
    dp[box] = count
    max_cnt = max(max_cnt, count)
print(max_cnt)