n, k = map(int, input().split())
removed = [0 for _ in range(n+1)]
i = 0
b = True
for j in range(2, n+1):
    if b and removed[j] == 0:
        loc = j
        while loc < n + 1:
            if removed[loc] == 0:
                i += 1
                removed[loc] = 1
                if i == k:
                    b = False
                    break
            
            loc += j
print(loc)
                