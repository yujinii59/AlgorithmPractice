def solution(survey, choices):
    personality = {'RT':{'R':0,'T':0},
               'CF':{'C':0,'F':0},
               'JM':{'J':0,'M':0},
               'AN':{'A':0,'N':0}
              }

    for types, choice in zip(survey, choices):
        kind = ''.join(sorted(types))
        score = choice - 4
        if score < 0:
            personality[kind][types[0]] += abs(score)
        elif score > 0:
            personality[kind][types[1]] += abs(score)

    rst = ''
    for psn in personality.values():
        psn = sorted(psn.items(), key=lambda x:[-x[1], x[0]])
        rst += psn[0][0]
        
    return rst