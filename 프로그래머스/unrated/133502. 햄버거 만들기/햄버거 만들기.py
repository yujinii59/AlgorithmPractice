def solution(ingredient):
    answer = 0
    seq = ''
    for num in ingredient:
        seq += str(num)
        if len(seq) >= 4:
            if seq[-4:] == '1231':
                answer += 1
                seq = seq[:-4]
    return answer