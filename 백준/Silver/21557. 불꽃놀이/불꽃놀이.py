from math import ceil

n = int(input())
dummy = list(map(int, input().split()))
print(max(dummy[0]-(n-2), dummy[-1]-(n-2), ceil((dummy[0]+dummy[-1]-(n-1)) / 2)))