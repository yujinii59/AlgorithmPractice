def solution(s):
    alphabets = {}
    answer = []
    for i, a in enumerate(s):
        idx = alphabets.get(a, -1)
        if idx == -1:
            answer.append(-1)
        else:
            answer.append(i-idx)
        alphabets[a] = i
    return answer