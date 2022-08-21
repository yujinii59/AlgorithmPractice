i = 0
while True:
    i += 1
    n = int(input())
    if n == 0:
        break
        
    names = {i+1: input() for i in range(n)}
    earring = set()
    for _ in range(2*n - 1):
        num, rand = input().split()
        if num in earring:
            earring.remove(num)
        else:
            earring.add(num)
            
    print(i, names[int(list(earring)[0])])