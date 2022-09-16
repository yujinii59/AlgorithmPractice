import sys

n, s = map(int, input().split())
cows = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)
cnt = 0
end = n-1
for i in range(n):
    cow = cows[i]
    if end <= i:
        cnt += (n-1) - i
    else:
        cnt += (n-1) - end
        for j in range(end, i, -1):
            if cow + cows[j] <= s:
                cnt += 1
            else:
                end = j
                break
print(cnt)