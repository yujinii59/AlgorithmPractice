n = int(input())
for _ in range(n):
    string = input()
    rst = ''
    prev = ''
    for s in string:
        if s != prev:
            rst += s
            prev = s
    print(rst)
        