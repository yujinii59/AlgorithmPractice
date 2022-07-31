cnt = [0,0]
target = 0
s = input()
prev = s[0]
for ss in s:
    if ss != prev:
        cnt[target] += 1
        target = (target + 1) % 2
        prev = ss
print(max(cnt))