n = int(input())
cnt = 0
for _ in range(n):
    if int(input()[2:]) <= 90:
        cnt += 1
        
print(cnt)