def solution(a, b, n):
    answer = 0
    while n >= a:
        q, r = divmod(n, a)
        n = q*b + r
        answer += q*b
    return answer