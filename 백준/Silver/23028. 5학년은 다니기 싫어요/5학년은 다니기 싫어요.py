from math import ceil

n, a, b = map(int, input().split())
n = 8-n
a = ceil((66-a) / 3)
b = ceil((130-b) / 3)
for _ in range(10):
    x, y = map(int, input().split())
    if n:
        n -= 1
        a -= x
        b -= min(6, x+y)
if a <= 0 and b <= 0:
    print('Nice')
else:
    print('Nae ga wae')