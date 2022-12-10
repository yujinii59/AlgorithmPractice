ls = input().split()
n = int(ls[0])
i = 0
arr = []
for elem in ls[1:]:
    arr.append(int(elem[::-1]))
    i += 1
    
while i < n:
    for elem in  input().split():
        arr.append(int(elem[::-1]))
        i += 1
        
print(*sorted(arr), sep='\n')