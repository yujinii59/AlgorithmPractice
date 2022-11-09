import sys

input = sys.stdin.readline

n = int(input())
employee = {}
cnt = 0
for _ in range(n):
    name, p = input().split()
    if p == '+':
        if employee.get(name, 0):
            employee[name] += 1
        else:
            employee[name] = 1
    else:
        if employee.get(name, 0):
            employee[name] -= 1
        else:
            cnt += 1
cnt += sum(employee.values())
print(cnt)