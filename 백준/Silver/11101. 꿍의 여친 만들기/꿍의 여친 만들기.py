n = int(input())
for _ in range(n):
    string = input().replace(',',',"').replace(':','":')
    kinds = eval('{"'+string+'}')
    conditions = input().split('|')
    times = sum(kinds.values())
    for condition in conditions:
        time = 0
        for cnd in condition.split('&'):
            time = max(time, kinds[cnd])
        times = min(times, time)
    print(times)