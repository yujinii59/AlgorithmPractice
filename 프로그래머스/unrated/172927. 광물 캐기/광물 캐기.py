def solution(picks, minerals):
    answer = 0
    pick_cnt = sum(picks)
    length = len(minerals)
    if length % 5:
        max_cnt = length // 5 + 1
    else:
        max_cnt = length // 5
    cases = []
    for i in range(min(pick_cnt, max_cnt)):
        cnts = [0,0,0]
        end = min(5*(i+1), length)
        for mineral in minerals[5*i:end]:
            if mineral == 'diamond':
                cnts[0] += 1
            elif mineral == 'iron':
                cnts[1] += 1
            else:
                cnts[2] += 1
        cases.append(cnts)
        
    cases = sorted(cases, reverse=True)
    for case in cases:
        if picks[0] > 0:
            answer += sum(case)
            picks[0] -= 1
        elif picks[1] > 0:
            answer += case[0]*5 + case[1] + case[2]
            picks[1] -= 1
        else:
            answer += case[0]*25 + case[1]*5 + case[2]
            picks[2] -= 1
    return answer