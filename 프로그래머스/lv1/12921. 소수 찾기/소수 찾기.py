def solution(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    else:
        answer = 1
        prime = [2]
        res = list(range(3, n+1, 2))
        while res[0] <= n**0.5:
            min_num = res[0]
            prime.append(min_num)
            res = sorted(list(set(res[1:]) - set(list(range(min_num**2, n+1, min_num)))))
        
        return len(prime) + len(res)