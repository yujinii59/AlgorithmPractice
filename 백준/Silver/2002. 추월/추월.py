from collections import deque

n = int(input())
seq = deque([input() for _ in range(n)])
cars = set()
cnt = 0
car = seq.popleft()
for _ in range(n):
    out = input()
    while True:
        if car != out:
            if car in cars:
                if seq:
                    car = seq.popleft()
                else:
                    car = ''
                continue
            else:
                cnt += 1
                break
        else:
            if seq:
                car = seq.popleft()
            else:
                car = ''
            break
    cars.add(out)
print(cnt)