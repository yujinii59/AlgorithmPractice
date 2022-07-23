stack = []
res = 0
for _ in range(int(input())):
    n = int(input())
    pop_cnt = 0
    while stack and stack[-1][0] > n:
        x, y = stack.pop()
        res = max(res, x * (y+pop_cnt))
        pop_cnt += y
    if not stack or stack[-1][0] < n:
        stack.append([n, pop_cnt + 1])
    else:
        stack[-1][1] += pop_cnt + 1
pop_cnt = 0
while stack:
    a, b = stack.pop()
    res = max(res, a * (b + pop_cnt))
    pop_cnt += b
print(res)