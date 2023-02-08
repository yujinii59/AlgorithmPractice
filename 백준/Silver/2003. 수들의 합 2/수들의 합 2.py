n, m = map(int, input().split())
seq = list(map(int, input().split()))

total = 0
start = 0
cnt = 0

for i in range(n):
    total += seq[i]
    while total > m:
        total -= seq[start]
        start += 1
        
    if total == m:
        cnt += 1
        
print(cnt)