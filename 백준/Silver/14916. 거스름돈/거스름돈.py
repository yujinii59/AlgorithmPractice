n = int(input())
cnt = -1
for i in range(n // 5, -1, -1):
    if (n - (5 * i)) % 2 == 0:
        cnt = i + (n - 5 * i) // 2
        break
print(cnt)