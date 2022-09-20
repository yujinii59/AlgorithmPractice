n = int(input())
houses = sorted(list(map(int, input().split())))
if n % 2:
    print(houses[n//2])
else:
    print(houses[n//2-1])
