import sys

input = sys.stdin.readline

n = int(input())
s = []
score = 0
for _ in range(n):
    infos = input().rstrip()
    a, t = 0, 1
    if infos == '0':
        if s:
            a, t = s.pop()
    else:
        a, t = list(map(int, infos.split()))[1:]
    
    t -= 1
    if t == 0:
        score += a
    else:
        s.append((a, t))
print(score)