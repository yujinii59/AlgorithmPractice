n, a, b = map(int, input().split())
n %= a
for _ in range(b):
    q, n = divmod(n*10, a)
    
print(q)