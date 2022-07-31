board = input()
l = len(board)
ss = ''
cnt = 0
boolean = True
for i, b in enumerate(board):
    if b == 'X':
        cnt += 1
        if i == l - 1:
            if cnt % 2 == 1:
                boolean = False
                break
            ss += 'AAAA' * (cnt // 4) + 'BB' * ((cnt % 4) // 2)
    else:
        if cnt % 2 == 1:
            boolean = False
            break
        if cnt > 0:
            ss += 'AAAA' * (cnt // 4) + 'BB' * ((cnt % 4) // 2)
            cnt = 0
        ss += '.'
        
if boolean:
    print(ss)
else:
    print(-1)