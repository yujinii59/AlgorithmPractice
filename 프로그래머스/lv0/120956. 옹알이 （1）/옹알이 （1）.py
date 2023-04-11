def solution(babbling):
    answer = 0
    pron = ["aya", "ye", "woo", "ma"]
    while babbling:
        tmp = []
        for word in babbling:
            if len(word) > 2 and word[:3] in ["aya","woo"]:
                if len(word) == 3:
                    answer += 1
                else:
                    tmp.append(word[3:])
            elif len(word) > 1 and word[:2] in ["ye","ma"]:
                if len(word) == 2:
                    answer += 1
                else:
                    tmp.append(word[2:])
        babbling = tmp
    return answer