n = int(input())
seq = list(map(int, input().split()))
max_length = 1
prev = seq[0]
length = 1
state = '.'
for s in seq[1:]:
    if prev < s:
        if state == '-':
            length = 2
        else:
            length += 1
        max_length = max(max_length, length)
        state = '+'
    elif prev == s:
        length = 1
        state = '.'
    else:
        length += 1
        state = '-'
        max_length = max(max_length, length)
    prev = s
print(max_length)