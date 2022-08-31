n = int(input())
rates = [0.04, 0.11, 0.23, 0.4, 0.6, 0.77, 0.89, 0.96, 1]
scores = sorted(list(map(int, input().split())), reverse=True)
rst = [0] * 9
prev = scores[0]
rnk = 0
for i, score in enumerate(scores):
    if score == prev:
        rst[rnk] += 1
    else:
        rate = (i+1) / n
        if rate <= 0.04:
            rst[0] += 1
            rnk = 0
        elif rate <= 0.11:
            rst[1] += 1
            rnk = 1
        elif rate <= 0.23:
            rst[2] += 1
            rnk = 2
        elif rate <= 0.4:
            rst[3] += 1
            rnk = 3
        elif rate <= 0.6:
            rst[4] += 1
            rnk = 4
        elif rate <= 0.77:
            rst[5] += 1
            rnk = 5
        elif rate <= 0.89:
            rst[6] += 1
            rnk = 6
        elif rate <= 0.96:
            rst[7] += 1
            rnk = 7
        else:
            rst[8] += 1
            rnk = 8
    prev = score
print(*rst, sep='\n')