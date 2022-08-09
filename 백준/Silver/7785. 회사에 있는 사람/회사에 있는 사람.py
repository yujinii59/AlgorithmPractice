n = int(input())
company = {}
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        company[name] = 'enter'
    else:
        del company[name]
        
for name in sorted(company.keys(), reverse=True):
    print(name)