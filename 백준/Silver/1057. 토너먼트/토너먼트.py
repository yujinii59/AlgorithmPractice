n, a, b = map(int, input().split())
a, b = a-1, b-1

cnt = 0
while True:
    cnt += 1
    if a // 2 == b // 2:
        print(cnt)
        break
    else:
        a //= 2
        b //= 2