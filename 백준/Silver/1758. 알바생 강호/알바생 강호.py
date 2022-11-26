n = int(input())
tips = sorted(list(int(input()) for _ in range(n)), reverse=True)
tip = 0
for i in range(n):
    if tips[i]-i <= 0:
        break
    tip += tips[i]-i
    
print(tip)