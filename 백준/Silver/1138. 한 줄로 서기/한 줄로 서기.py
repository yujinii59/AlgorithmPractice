n = int(input())
num_of_taller = list(map(int, input().split()))
seq = []
for i, num in enumerate(num_of_taller[::-1]):
    if not seq:
        seq.append(n-i)
    else:
        j = 0
        while num:
            height = seq[j]
            if height > n-i:
                num -= 1
            j += 1
                
        seq = seq[:j] + [n-i] + seq[j:]
print(*seq)