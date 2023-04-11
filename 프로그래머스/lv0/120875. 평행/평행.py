from itertools import combinations

def solution(dots):
    answer = 0
    cases = combinations(list(range(4)), 2)
    grad = dict()
    for case in cases:
        opp = []
        for i in range(4):
            if i not in case:
                opp.append(i)
        
        x1, y1 = dots[case[0]]
        x2, y2 = dots[case[1]]
        if x2 == x1:
            grad[case] = 'inf'
        else:
            grad[case] = (y2-y1) / (x2-x1)
            
        if grad.get(tuple(opp), 0) and grad[case] == grad[tuple(opp)]:
            answer = 1
            break
    
    return answer