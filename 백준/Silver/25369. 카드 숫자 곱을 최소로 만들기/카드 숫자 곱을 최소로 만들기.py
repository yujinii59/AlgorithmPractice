from itertools import combinations_with_replacement

n = int(input())
cases = combinations_with_replacement(list(range(1, 10)), n)
A = list(map(int, input().split()))
mult = 1
for num in A:
    mult *= num

b = True
for case in cases:
    mult_B = 1
    for num in case:
        mult_B *= num
        
    if mult_B > mult:
        print(*case)
        b = False
        break
if b:
    print(-1)