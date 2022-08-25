t = int(input())
for _ in range(t):
    n = int(input())
    real = set(map(int, input().split()))
    m = int(input())
    test = list(map(int, input().split()))
    for num in test:
        if num in real:
            print(1)
        else:
            print(0)