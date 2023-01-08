from collections import deque

n, w, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = {}
weights = 0
time = 1
truck = trucks.popleft()
while truck:
    weights -= bridge.get(time, 0)
    if truck:
        if weights + truck <= L:
            bridge[time+w] = truck
            weights += truck
            if trucks:
                truck = trucks.popleft()
            else:
                truck = 0
    else:
        break
    time += 1
print(max(bridge.keys()))
            