from itertools import permutations

n = int(input())
k = int(input())
numbers = [input() for _ in range(n)]
cases = permutations(numbers, k)
ints = set()
for case in cases:
    ints.add(''.join(case))

print(len(list(ints)))