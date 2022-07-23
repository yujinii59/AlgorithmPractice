def prime_numbers(num):
    if num < 2:
        result = []
    elif num == 2:
        result = [2]
    else:
        whole = list(range(3, num+1, 2))
        rm = []
        result = [2]
        for i in range(3, int(num ** 0.5) + 1, 2):
            rm.extend(list(range(i*i, int(num ** 0.5) + 1, i)))
        result.extend(sorted(list(set(whole) - set(rm))))
    return result
        

t = int(input())
for k in range(t):
    n = int(input())
    primes = prime_numbers(n)
    cnt = 0
    for i in range(1, n+1):
        num = i
        divisor = 1
        for prime in primes:
            if num == 1:
                break
            c = 0
            while num > 1:
                if num % prime == 0:
                    c += 1
                    num //= prime
                else:
                    break
            divisor *= (c + 1)
        if divisor % 2 == 1:
            cnt += 1
    print(cnt)
                