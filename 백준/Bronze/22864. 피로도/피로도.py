a, b, c, m = map(int, input().split())
amount = 0
time = 24
res = m
while time > 0:
    work_time = min(time, res // a)
    amount += work_time * b
    res -= work_time * a
    time -= work_time
    res = min(m, res+c)
    time -= 1
print(amount)