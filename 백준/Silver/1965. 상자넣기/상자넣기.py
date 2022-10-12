n = int(input())
seq = list(map(int, input().split()))
max_length = 1
case = {}
for num in seq:
    if num not in case:
        case[num] = 1
    
    for n in case:
        if n < num:
            case[num] = max(case[num], case[n] + 1)
            max_length = max(max_length, case[num])
            
print(max_length)