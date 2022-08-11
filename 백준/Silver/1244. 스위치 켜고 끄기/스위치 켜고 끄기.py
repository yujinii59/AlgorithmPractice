n = int(input())
switches = [0] + list(map(int, input().split()))
k = int(input())
for _ in range(k):
    gen, num = map(int, input().split())
    if gen == 1:
        cnt = n // num
        for i in range(cnt):
            switches[num * (i+1)] = (switches[num * (i+1)] + 1) % 2
            
    else:
        start = num
        end = num
        switches[num] = (switches[num] + 1) % 2
        while True:
            if start - 1 < 1 or end + 1 > n:
                break
            
            start -= 1
            end += 1
            if switches[start] == switches[end]:
                switches[start] = (switches[start] + 1) % 2
                switches[end] = (switches[end] + 1) % 2
            else:
                break

l = n // 20
for i in range(l+1):
    print(*switches[(i * 20)+1: (i * 20) + 21])