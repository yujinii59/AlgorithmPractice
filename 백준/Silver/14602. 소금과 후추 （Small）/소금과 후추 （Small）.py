r,c,k,w = map(int,input().split())
pickcels = [list(map(int, input().split())) for _ in range(r)]
if w == 1:
    for row in pickcels:
        print(*row)
else:
    for i in range(r-w+1):
        for j in range(c-w+1):
            pic = []
            for k in range(w):
                pic.extend(pickcels[i+k][j:j+w])

            pic = sorted(pic)[w**2 // 2]
            print(pic, end=' ')
        print()