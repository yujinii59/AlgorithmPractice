num_ls = list(map(int, list(input())))
if sum(num_ls) % 3 > 0:
    print(-1)
else:
    num_dict = {i:0 for i in range(9, -1, -1)}
    for num in num_ls:
        num_dict[num] += 1
    if num_dict[0] == 0:
        print(-1)
    else:
        for n, cnt in num_dict.items():
            print(str(n) * cnt, end='')