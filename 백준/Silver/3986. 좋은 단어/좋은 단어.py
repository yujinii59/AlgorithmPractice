n = int(input())
cnt = n
for _ in range(n):
    string = list(input())
    tmp = ['']
    for s in string:
        if s == tmp[-1]:
            tmp.pop()
        else:
            tmp.append(s)
    if len(tmp) > 1:
        cnt -= 1
            
print(cnt)