n = int(input())
cnt = 0
names = set()
for _ in range(n):
    name = input()
    if name == 'ENTER':
        names.clear()
        
    else:
        if name not in names:
            cnt += 1
            names.add(name)
            
print(cnt)