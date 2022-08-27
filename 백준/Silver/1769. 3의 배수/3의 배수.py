num = input()
cnt = 0
while int(num) >= 10:
    cnt += 1
    convert = 0
    for n in num:
        convert += int(n)
        
    num = str(convert)

print(cnt)
if int(num) % 3 == 0:
    print('YES')
else:
    print('NO')