t = int(input())
for i in range(t):
    cnt = 0
    seq = list(map(int, input().split()))
    subsets = []
    prev = seq[0]
    for num in seq[1:]:
        tmp = []
        for subset in subsets:
            start, min_val = subset
            if num <= start:
                cnt += 1
            else:
                if min_val > num:
                    cnt += 1
                    min_val = num
                tmp.append((start, min_val))
        subsets = tmp
        
        if num > prev:
            subsets.append((prev, num))
        prev = num
    if subsets:
        cnt += len(subsets)
            
    print(i+1, cnt)