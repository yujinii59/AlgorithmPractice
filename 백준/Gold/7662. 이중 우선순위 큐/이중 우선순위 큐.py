import heapq
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    max_hp = []
    min_hp = []
    current = {}
    for _ in range(n):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(max_hp, -num)
            heapq.heappush(min_hp, num)
            if current.get(num, 0):
                current[num] += 1
            else:
                current[num] = 1

        else:
            if len(current) == 0:
                continue

            if num == -1:
                while True:
                    p = heapq.heappop(min_hp)
                    if current.get(p, 0):
                        current[p] -= 1
                        if current[p] == 0:
                            del current[p]
                        break
            else:
                while True:
                    p = -heapq.heappop(max_hp)
                    if current.get(p, 0):
                        current[p] -= 1
                        if current[p] == 0:
                            del current[p]
                        break
    if len(current):
        sort = sorted(current.keys())
        print(sort[-1], sort[0])
    else:
        print('EMPTY')
