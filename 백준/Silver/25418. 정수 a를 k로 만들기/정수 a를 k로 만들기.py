a, k = map(int, input().split())
cnt = 0
while k > a:
    cnt += 1
    if k % 2:
        k -= 1
    else:
        if k // 2 >= a:
            k //= 2
        else:
            k -= 1
print(cnt)