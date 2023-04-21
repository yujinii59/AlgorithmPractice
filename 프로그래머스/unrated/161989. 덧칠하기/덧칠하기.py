def solution(n, m, section):
    answer = 0
    end = 0
    for num in section:
        if end < num:
            answer += 1
            end = num + m - 1
    return answer