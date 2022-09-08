key = sorted([(s, i) for i, s in enumerate(list(input()))])
l = len(key)
string = input()
L = len(string)
h = L // l
rst = ['']*L
for i, (s, c) in enumerate(key):
    for r in range(h):
        rst[l*r+c] = string[h*i+r]
print(*rst,sep='')