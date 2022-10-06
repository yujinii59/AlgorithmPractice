n = int(input())
q, r = divmod(n-1,4)
if q % 2:
    print(5-r)
else:
    print(r+1)