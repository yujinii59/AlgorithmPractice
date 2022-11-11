from itertools import product

t = int(input())
for _ in range(t):
    numbers = set()
    seq = []
    for _ in range(3):
        n = int(input())
        seq.append(list(set(map(int, input().split()))))
        
    cases = product(seq[0], seq[1], seq[2])
    for case in cases:
        num = sum(case)
        if set(str(num)) | set(['5','8']) == set(['5','8']):
            numbers.add(num)
    print(len(numbers))