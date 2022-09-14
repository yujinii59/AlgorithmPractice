def solution(n, k):
    num = convert(n, k)
    cases = num.split('0')
    cnt = 0
    for case in cases:
        if case == '':
            continue
        if is_prime(int(case)):
            cnt += 1
    return cnt

def convert(n, k):
    num = ''
    while n:
        n, r = divmod(n, k)
        num = str(r) + num
    return num

def is_prime(n):
    if n == 1:
        return False
    elif n % 2 == 0:
        if n == 2:
            return True
        else:
            return False
    else:
        for i in range(3,int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False

        return True