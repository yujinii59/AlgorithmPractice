t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]]
    max_sum = arr[0]
    for num in arr[1:]:
        dp.append(0)
        tmp = []
        for h in dp:
            tmp.append(h+num)
            max_sum = max(max_sum, h+num)
        dp = tmp
            
    print(max_sum)