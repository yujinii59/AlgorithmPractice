def solution(t, p):
    t_len = len(t)
    p_len = len(p)
    if t_len < p_len:
        return 0
    answer = 0
    num = ' ' + t[:p_len-1]
    for i in range(p_len-1, t_len):
        num = num[1:] + t[i]
        if num <= p:
            answer += 1
    return answer