n = int(input())
seq_A = list(map(int, input().split()))
seq = {}
max_len = 0
for num in seq_A:
    if num not in seq:
        seq[num] = 1
    for k, v in seq.items():
        if k > num:
            seq[num] = max(seq[num], v + 1)
    max_len = max(max_len, seq[num])
print(max_len)    