import sys

s = sys.stdin.readline().rstrip()
ls = []
for i in range(1, len(s) + 1):
    for j in range(0, len(s) - (i - 1)):
        ls.append(s[j:j + i])
ls = set(ls)
print(len(ls))