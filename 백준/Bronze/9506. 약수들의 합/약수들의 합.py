while True:
    n = int(input())
    if n == -1:
        break
        
    div = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if i > 1:
                div.append(n // i)
    div = sorted(div)        
    if sum(div) == n:
        print(f'{n} = ',end='')
        print(*div, sep=' + ')
    else:
        print(f'{n} is NOT perfect.')
        