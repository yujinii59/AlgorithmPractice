n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.extend(list(map(int, input().split())))
print(*sorted(arr))