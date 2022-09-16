t = int(input())
for _ in range(t):
    h, l = map(int, input().split())
    cars = {}
    max_num = 0
    for i in range(h):
        parked = list(map(int, input().split()))
        for j, park in enumerate(parked):
            if park != -1:
                cars[park] = (i, j)
                max_num = max(max_num, park)
    states = {i: 0 for i in range(h)}
    times = 0
    for num in range(1, max_num+1):
        floor, loc = cars[num]
        state = states[floor]
        times += 20 * floor
        move = 0
        if loc > state:
            move = min(loc-state, l-loc+state)
        elif loc < state:
            move = min(state-loc, l-state+loc)
        times += 5 * move
        states[floor] = loc
    print(times)