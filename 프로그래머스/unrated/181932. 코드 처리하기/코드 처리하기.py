def solution(code):
    answer = ''
    mode = 0
    for i, s in enumerate(code):
        if s == '1':
            mode += 1
            mode %= 2
        else:
            if i % 2 == mode:
                answer += s
    if answer == '':
        answer = 'EMPTY'
    return answer