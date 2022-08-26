n = int(input())
cases = [0]
for i in range(1, n + 1):
    if i == 1:
        cases.append(1)
    elif i == 2:
        cases.append(cases[1] + 2)
    else:
        cases.append(1 * cases[i - 1] + 2 * cases[i - 2])
cnt = cases[n] % 10007
print(cnt)