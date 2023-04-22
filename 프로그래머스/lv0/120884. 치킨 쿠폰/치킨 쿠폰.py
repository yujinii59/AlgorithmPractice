def solution(chicken):
    answer = 0
    while chicken >= 10:
        q, r = divmod(chicken, 10)
        chicken = q + r
        answer += q
    return answer