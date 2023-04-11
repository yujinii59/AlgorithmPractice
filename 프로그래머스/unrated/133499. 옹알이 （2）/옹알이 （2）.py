def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for p in pron:
            if p * 2 not in word:
                word = word.replace(p, ' ')
        if word.strip() == '':
            answer += 1
    return answer