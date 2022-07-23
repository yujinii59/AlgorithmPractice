n, m = map(int, input().split())
b = True
for _ in range(m):
    k = int(input())
    books = list(map(int, input().split()))
    if b:
        for i in range(k-1):
            if books[i] < books[i+1]:
                b = False
                break
    

if b:
    print('Yes')
else:
    print('No')