arr = {i+1:[] for i in range(1000)}
n = int(input())
a = list(map(int, input().split()))
for i, e in enumerate(a):
    arr[e].append(i)
    
num = 0
results = [0 for _ in range(n)]
for i, ls in arr.items():
    if len(ls) > 0:
        for j in ls:
            results[j] = num
            num += 1
print(*results)