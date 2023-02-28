from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    if nums == [0]:
        break
    k, s = nums[0], nums[1:]
    cases = combinations(s, 6)
    for case in cases:
        print(*case)
        
    print()