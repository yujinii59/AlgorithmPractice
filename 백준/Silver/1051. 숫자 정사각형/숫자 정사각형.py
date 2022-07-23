n, m = map(int, input().split())
size = 1
rec = [list(map(int, list(input()))) for _ in range(n)]
for i in range(n):
    for j in range(m):
        num = rec[i][j]
        for k in range(j+1, m):
            if num == rec[i][k]:
                diff = k-j
                if i+diff >= n:
                    continue
                if num == rec[i+diff][j] and num == rec[i+diff][k]:
                    size = max(size, (diff+1) ** 2)
print(size)