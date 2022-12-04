import datetime

n = int(input())
person = []
for _ in range(n):
    name, d, m, y = input().split()
    days = datetime.datetime.now() - datetime.datetime(year=int(y), month=int(m), day=int(d))
    days = days.days
    person.append((days, name))
    
person = sorted(person)
print(person[0][1])
print(person[-1][1])