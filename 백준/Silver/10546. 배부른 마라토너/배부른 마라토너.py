n = int(input())
parti = {}
for _ in range(n):
    name = input()
    if parti.get(name, 0):
        parti[name] += 1
    else:
        parti[name] = 1

for _ in range(n-1):
    name = input()
    parti[name] -= 1
    if parti[name] == 0:
        del parti[name]
        
print(*parti.keys())