n = int(input())
sizes = []
rnk = {}
for i in range(n):
    weight, height = map(int, input().split())
    sizes.append((weight, height))
    rnk[(weight, height)] = 1

cases = list(set(sizes))
for j in range(len(cases)):
    w, h = cases[j]
    for case in (cases[j + 1:]):
        case_w, case_h = case
        if case_w > w and case_h > h:
            rnk[(w, h)] += 1
        elif case_w < w and case_h < h:
            rnk[(case_w, case_h)] += 1
for wgt, hgt in sizes:
    rank = rnk[(wgt, hgt)]
    print(rank, end=' ')