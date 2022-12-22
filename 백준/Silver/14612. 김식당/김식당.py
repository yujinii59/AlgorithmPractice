n, m = map(int, input().split())
dic = {}
ls = []
for _ in range(n):
    inp = input().split()
    length = len(inp)
    if length == 1:
        ls = sorted(ls, key=lambda x: [dic[x], x])
    elif length == 2:
        ls.remove(int(inp[1]))
        del dic[int(inp[1])]
    else:
        dic[int(inp[1])] = int(inp[2])
        ls.append(int(inp[1]))
        
    if ls:
        for elem in ls:
            print(elem, end=' ')
        print()
    else:
        print('sleep')