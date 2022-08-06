x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
inf = int(1e10)
a_b = ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5
if x_a != x_b:
    a_b_incli = abs((y_a - y_b) / (x_a - x_b))
else:
    a_b_incli = inf
a_c = ((x_a - x_c) ** 2 + (y_a - y_c) ** 2) ** 0.5
if x_a != x_c:
    a_c_incli = abs((y_a - y_c) / (x_a - x_c))
else:
    a_c_incli = inf
c_b = ((x_c - x_b) ** 2 + (y_c - y_b) ** 2) ** 0.5
if x_c != x_b:
    c_b_incli = abs((y_c - y_b) / (x_c - x_b))
else:
    c_b_incli = inf
length = sorted([a_b, a_c, c_b])

if a_b_incli == a_c_incli == c_b_incli:
    print(-1.0)
else:
    diff = sum(length[1:]) - sum(length[:2])
    print(diff * 2)