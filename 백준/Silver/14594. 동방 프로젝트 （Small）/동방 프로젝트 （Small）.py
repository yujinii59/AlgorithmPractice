n = int(input())
m = int(input())
break_wall = set()
for _ in range(m):
    x, y = map(int, input().split())
    break_wall = break_wall.union(set(list(range(x, y))))
    
print(n-len(break_wall))