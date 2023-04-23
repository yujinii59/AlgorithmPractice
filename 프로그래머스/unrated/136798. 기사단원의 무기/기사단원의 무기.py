def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        tmp = []
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                if j ** 2 == i:
                    tmp.append(j)
                else:
                    tmp.append(j)
                    tmp.append(i//j)
        length = len(tmp)
        if length > limit:
            answer += power
        else:
            answer += length
    return answer