n = int(input())
times = list(map(int, input().split()))

total = 0
time_total = 0
for time in sorted(times):
    time_total += total + time
    total += time
    
print(time_total)