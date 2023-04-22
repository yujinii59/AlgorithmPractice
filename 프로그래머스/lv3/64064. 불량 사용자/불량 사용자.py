def solution(user_id, banned_id):
    user_len = {}
    for user in user_id:
        ids = user_len.get(len(user), [])
        ids.append(user)
        user_len[len(user)] = ids
    
    cases = [set()]
    for ban in banned_id:
        idx = []
        id_tmp = ''
        for i, alpha in enumerate(ban):
            if alpha == '*':
                idx.append(i)
            else:
                id_tmp += alpha
        
        length = len(ban)
        tmp = []
        for user in user_len.get(length, []):
            conv = ''
            prev = 0
            for i in idx:
                conv += user[prev:i]
                prev = i+1
            conv += user[prev:]
            if conv == id_tmp:
                for case in cases:
                    if user not in case:
                        case_tmp = case.copy()
                        case_tmp.add(user)
                        if case_tmp not in tmp:
                            tmp.append(case_tmp)
        cases = tmp
        
    return len(cases)