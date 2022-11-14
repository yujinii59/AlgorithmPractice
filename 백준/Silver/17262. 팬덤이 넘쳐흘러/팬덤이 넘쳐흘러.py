import sys
input = sys.stdin.readline

n = int(input())
max_s = 0
min_e = 100000
for _ in range(n):
    s, e = map(int, input().split())
    max_s = max(s, max_s)
    min_e = min(e, min_e)
    
if max_s <= min_e:
    time = 0
else:
    time = max_s - min_e

print(time)