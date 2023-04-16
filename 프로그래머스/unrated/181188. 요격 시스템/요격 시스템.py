def solution(targets):
    targets = sorted(targets)
    end = 0
    cnt = 0
    for s,e in targets:
        if s >= end:
            cnt += 1
            end = e
        else:
            end = min(end, e)
    
    return cnt