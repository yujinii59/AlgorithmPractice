from collections import deque
import sys

n = int(input())
for _ in range(n):
    inp, rst = map(int, sys.stdin.readline().split())
    q = deque([(inp, '')])
    set_num = set([inp])
    while q:
        num, cmd = q.popleft()
        if num == rst:
            print(cmd)
            break
        
        # D
        d = (num * 2) % 10000
        if d not in set_num:
            set_num.add(d)
            q.append((d, cmd+'D'))
        
        # S
        s = (num - 1) % 10000
        if s not in set_num:
            set_num.add(s)
            q.append((s, cmd+'S'))
        
        # L
        div, res = divmod(num, 1000)
        l = res * 10 + div 
        if l not in set_num:
            set_num.add(l)
            q.append((l, cmd+'L'))
        
        # R
        div, res = divmod(num, 10)
        r = res * 1000 + div
        if r not in set_num:
            set_num.add(d)
            q.append((r, cmd+'R'))