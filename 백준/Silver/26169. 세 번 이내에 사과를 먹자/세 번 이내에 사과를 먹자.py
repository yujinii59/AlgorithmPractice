def move(cnt, apple, r, c, visited):
    global moves
    flag = False
    apple += boards[r][c]
    if cnt < 3:
        visited.add((r, c))
        for x, y in moves:
            mr = x+r
            mc = y+c
            if mr < 0 or mr >= 5 or mc < 0 or mc >= 5:
                continue
            if boards[mr][mc] >= 0 and (mr, mc) not in visited:
                flag = move(cnt+1, apple, mr, mc, visited)
                if flag:
                    break
    elif cnt == 3:
        if apple >= 2:
            flag = True
    return flag

boards = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
moves = [(-1,0),(0,-1), (1, 0), (0,1)]
flag = move(0, 0, r, c, set())
if flag:
    print(1)
else:
    print(0)