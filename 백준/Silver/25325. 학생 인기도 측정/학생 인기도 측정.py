n = int(input())
stud = {name:0 for name in input().split()}
for _ in range(n):
    for name in input().split():
        stud[name] += 1
        
stud = sorted(stud.items(), key=lambda x: [-x[1], x[0]])

for name, cnt in stud:
    print(name, cnt)