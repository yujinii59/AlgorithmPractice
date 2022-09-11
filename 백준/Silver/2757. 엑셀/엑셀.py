from string import ascii_uppercase

alpha = {i:a for i, a in enumerate(ascii_uppercase)}
while True:
    loc = input()
    idx = loc.index('C')
    r, c = loc[1:idx], int(loc[idx+1:])
    if r == '0' and c == 0:
        break
    rst = r
    while True:
        c -= 1
        res = c % 26
        rst = alpha[res] + rst
        c = c // 26
        if c == 0:
            break
    print(rst)