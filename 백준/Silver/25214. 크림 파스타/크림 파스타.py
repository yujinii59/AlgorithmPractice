n = int(input())
arr = list(map(int, input().split()))
answer = [0]
min_prev = arr[0]
max_prev = arr[0]
max_diff = 0
for num in arr[1:]:
    if num < min_prev:
        min_prev = num
        max_prev = num
    elif num > max_prev:
        max_prev = num
        max_diff = max(max_diff, max_prev - min_prev)
    answer.append(max_diff)
print(*answer)