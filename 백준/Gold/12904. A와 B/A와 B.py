s = input()
t = list(input())
while len(t) > len(s):
    last = t[-1]
    if last == 'A':
        t = t[:-1]
    else:
        t = t[:-1][::-1]
if ''.join(t) == s:
    print(1)
else:
    print(0)