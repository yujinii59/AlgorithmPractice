from math import ceil

n = int(input())
cum_time = {}
for _ in range(n):
    time, name = input().split()
    h, m = map(int, time.split(':'))
    time = h*60 + m
    if cum_time.get(name, 0):
        cum_time[name] += time
    else:
        cum_time[name] = time

total_fees = {}
for name, time in cum_time.items():
    if time <= 100:
        total_fees[name] = 10
    else:
        time -= 100
        total_fees[name] = 10 + ceil(time / 50) * 3
        
total_fees = sorted(total_fees.items(), key=lambda x:[-x[1], x[0]])
for name, fee in total_fees:
    print(name, fee)