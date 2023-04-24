from collections import Counter

def solution(k, m, score):
    answer = 0
    counter = Counter(score)
    res = 0
    for i in range(k, 0, -1):
        cnt = counter.get(i, 0)
        q, r = divmod(cnt, m)
        if r + res >= m:
            q += 1
            res = res+r-m
        else:
            res += r
            
        answer += q * i * m
        
    return answer