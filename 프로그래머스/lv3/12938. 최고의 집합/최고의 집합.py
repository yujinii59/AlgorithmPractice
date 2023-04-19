def solution(n, s):
    q, r = divmod(s, n)
    if q == 0:
        return [-1]
    answer = [q] * (n-r) + [q+1] * r
    return answer