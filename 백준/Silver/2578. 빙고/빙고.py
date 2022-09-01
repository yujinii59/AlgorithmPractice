board = {}
for i in range(5):
    numbers = list(map(int, input().split()))
    for j, num in enumerate(numbers):
        board[num] = (i, j)

called_num = []
for _ in range(5):
    called_num.extend(list(map(int, input().split())))

horizon = {i: 0 for i in range(5)}
vertical = {i: 0 for i in range(5)}
diagonal = {0: 0, 4: 0}
cnt = 0
for i, num in enumerate(called_num):
    x, y = board[num]
    horizon[x] += 1
    if horizon[x] == 5:
        cnt += 1

    vertical[y] += 1
    if vertical[y] == 5:
        cnt += 1

    if x == y:
        diagonal[0] += 1
        if diagonal[0] == 5:
            cnt += 1

    if x + y == 4:
        diagonal[4] += 1
        if diagonal[4] == 5:
            cnt += 1

    if cnt >= 3:
        print(i + 1)
        break