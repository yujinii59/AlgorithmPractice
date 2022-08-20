total = 0
min_diff = 100
pass_yn = False
for _ in range(10):
    score = int(input())
    if pass_yn:
        continue
    tmp = total + score
    if min_diff >= abs(100-tmp):
        total = tmp
        min_diff = abs(100-tmp)
    else:
        pass_yn = True
    
print(total)