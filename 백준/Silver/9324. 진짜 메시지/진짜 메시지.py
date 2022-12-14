n = int(input())
for _ in range(n):
    message = input()
    alpha = {}
    chk = ''
    for msg in message:
        cnt = alpha.get(msg, 0)
        if chk == '':
            if cnt % 3 == 2:
                chk = msg
            alpha[msg] = cnt + 1
        else:
            if msg != chk:
                print('FAKE')
                break
            chk = ''

    else:
        if chk == '':
            print('OK')
        else:
            print('FAKE')
