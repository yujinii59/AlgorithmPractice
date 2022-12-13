n, q = map(int, input().split())
rapid = list(map(int, input().split()))
amount = [abs(rapid[i]-rapid[i+1]) for i in range(n-1)]

for _ in range(q):
    s, e= map(int, input().split())
    if s >= e:
        print(0)
    else:
        print(sum(amount[s-1:e-1]))