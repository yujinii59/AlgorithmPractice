n = int(input())
r, c, v = map(int, input().split())
personal = []
rooms = []
for _ in range(n):
    x, y, e = map(int, input().split())
    personal.append((x, y, e))
    rooms.append((x,y))

max_vel = 0
for room in rooms:
    x, y = room
    vel = max(0, v - (abs(x-r) + abs(y-c)))
    for wifi in personal:
        if vel > 0:
            e = max(0, wifi[2] - (abs(x-wifi[0]) + abs(y-wifi[1])))
            if e > 0:
                vel = max(0, vel-e)
        else:
            break
    max_vel = max(max_vel, vel)
    
if max_vel:
    print(max_vel)
else:
    print('IMPOSSIBLE')