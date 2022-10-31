n = int(input())
rst = [[' '] * (2 * n) for _ in range(n)]
half = (2 * n) // 2
base = [[' ', ' ', '*', ' ', ' '], [' ', '*', ' ', '*', ' '], ['*', '*', '*', '*', '*']]
for i, row in enumerate(base):
    for j, elem in enumerate(row):
        rst[i][half - 2 + j] = elem


def stars(r):
    global rst
    if r % 2 == 0:
        stars(r // 2)
    if r < n:
        for sign in [-1, 1]:
            c = half + (sign * r)
            start_c = half

            for i in range(r):
                for j in range(1 - r, r):
                    rst[r + i][c + j] = rst[i][start_c + j]

    return None


stars(n)

for i in range(n):
    print(*rst[i][1:], sep='')
