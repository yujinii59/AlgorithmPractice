n = int(input())
case = [1]
for i in range(1, n + 1):
    if i == 1:
        case.append(1)
    else:
        case.append(case[i - 1] + case[i - 2])
        
print(case[n] % 10007)