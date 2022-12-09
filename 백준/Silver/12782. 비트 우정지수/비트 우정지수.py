n = int(input())
for _ in range(n):
    num1, num2 = input().split()
    cnt = 0
    one1 = 0
    one2 = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            if one2 > 0 and num1[i] == '1':
                one2 -= 1
            elif one1 > 0 and num2[i] == '1':
                one1 -= 1
            else:
                cnt += 1
                if num1[i] == '1':
                    one1 += 1
                else:
                    one2 += 1
    print(cnt)