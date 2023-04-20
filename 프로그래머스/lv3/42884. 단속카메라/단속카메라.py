def solution(routes):
    routes = sorted(routes)
    answer = 0
    out = -30001
    for s,e in routes:
        if s > out:
            answer += 1
            out = e
        else:
            out = min(out, e)
    
    return answer