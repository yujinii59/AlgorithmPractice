import sys

n = int(input())
times = {}
for i in range(n):
    x, y, v = map(int, sys.stdin.readline().split())
    times[i+1] = ((x ** 2 + y ** 2) ** 0.5) / v
    
times = sorted(times.items(), key=lambda x: [x[1],x[0]])
for num, _ in times:
    print(num)