def solution(number):
    answer = 0
    cases = []
    for num in number:
        tmp = [(num, 1)]
        for calc, cnt in cases:
            if cnt == 2:
                if num+calc == 0:
                    answer += 1
            else:
                tmp.append((calc+num, cnt+1))
        cases.extend(tmp)
                    
    
    return answer