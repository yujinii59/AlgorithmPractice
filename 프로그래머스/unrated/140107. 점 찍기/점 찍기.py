def solution(k, d):
    answer = 0
    sq = d ** 2
    for i in range(0, d+1, k):
        answer += ((sq - i**2) ** 0.5) // k + 1
    return answer