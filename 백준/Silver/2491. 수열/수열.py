n = int(input())
seq = list(map(int, input().split()))
max_len = 1
prev = seq[0]
sort = '.'
cnt = 1
same = 1
for num in seq[1:]:
    if prev < num:
        if sort == '-':
            cnt = same + 1
        else:
            cnt += 1
        same = 1
        sort = '+'
    elif prev == num:
        cnt += 1
        same += 1
    else:
        if sort == '+':
            cnt = same + 1
        else:
            cnt += 1
        same = 1
        sort = '-'
    max_len = max(max_len, cnt)
    prev = num
print(max_len)