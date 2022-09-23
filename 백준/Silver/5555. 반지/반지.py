string = input()
n = int(input())
cnt = 0
for _ in range(n):
    s = input() * 2
    if string in s:
        cnt += 1
print(cnt)