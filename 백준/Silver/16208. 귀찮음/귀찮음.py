n = int(input())
lengths = sorted(list(map(int, input().split())))
total = sum(lengths)
costs = 0
for length in lengths:
    costs += length * (total - length)
    total -= length
print(costs)