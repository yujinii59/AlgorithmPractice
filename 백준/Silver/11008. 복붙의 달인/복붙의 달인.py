n = int(input())
for _ in range(n):
    s, p = input().split()
    len_s = len(s)
    len_p = len(p)
    s = s.replace(p, '')
    sec = (len_s - len(s)) // len_p + len(s)
    print(sec)