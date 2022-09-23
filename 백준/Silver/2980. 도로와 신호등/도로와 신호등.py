n, l = map(int, input().split())
time = 0
loc = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    time += (d-loc)
    res = time % (r+g)
    if res < r:
        time += r-res
    loc = d
print(time + l-loc)