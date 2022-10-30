import sys

input = lambda: sys.stdin.readline().rstrip()

def solution(seq):
    nums = []
    temp = []
    for s in seq:
        if s.isalpha():
            if len(temp) > 0:
                nums.append(int(''.join(temp)))
                temp = []
        else:
            temp.append(s)
    if len(temp) > 0:
        nums.append(int(''.join(temp)))

    return nums


n = int(input())

results = []
for _ in range(n):
    seq = input()
    results.extend(solution(seq))

results = sorted(results)
print(*results, sep='\n')