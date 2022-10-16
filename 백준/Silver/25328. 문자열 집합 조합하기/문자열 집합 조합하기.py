from itertools import combinations

x = input()
y = input()
z = input()
k = int(input())
c_x = set(combinations(x, k))
c_y = set(combinations(y, k))
c_z = set(combinations(z, k))
rst = sorted(list((c_x & c_y) | (c_x & c_z) | (c_y & c_z)))
if rst:
    for ss in rst:
        print(''.join(ss))
else:
    print(-1)