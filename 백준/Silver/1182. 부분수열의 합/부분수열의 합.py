n, s = map(int, input().split())
cnt = 0
sums = [0]
for num in list(map(int, input().split())):
    tmp = []
    for summary in sums:
        tmp.append(summary+num)
        if summary + num == s:
            cnt += 1
    sums.extend(tmp)
print(cnt)