s = input()
p = 0
cnt = 0
for ss in s:
    if ss == '(':
        p += 1
    else:
        if p == 0:
            cnt += 1
        else:
            p -= 1
if p > 0:
    cnt += p
print(cnt)