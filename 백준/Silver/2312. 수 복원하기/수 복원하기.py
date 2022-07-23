from math import sqrt

def prime(num):
    primes = set(range(2, num + 1))
    rm = list(range(2 * 2, num + 1, 2))
    for i in range(3, int(sqrt(num)) + 1, 2):
        rm.extend(list(range(i * 2, num + 1, i)))
        
    primes = sorted(list(primes - set(rm)))  
    return primes

t = int(input())
for _ in range(t):
    n = int(input())
    primes = prime(n)
    for p in primes:
        i = 0
        while True:
            if n % p == 0:
                n //= p
                i += 1
            else:
                break
        if i > 0:
            print(p, i)
        if n == 1:
            break