def solution(sequence, k):
    accum = {0:-1}
    total = 0
    cnt = len(sequence) + 1
    answer = [-1,-1]
    for i, num in enumerate(sequence):
        if num > k:
            break
        total += num
        accum[total] = i
        if total >= k and accum.get(total-k, 0):
            if cnt > i-accum[total-k]:
                cnt = i-accum[total-k]
                answer = [accum[total-k]+1, i]
            
            
    return answer