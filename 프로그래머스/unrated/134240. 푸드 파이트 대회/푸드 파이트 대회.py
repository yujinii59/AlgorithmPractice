def solution(food):
    answer = ''
    for i, num in enumerate(food[1:]):
        cnt = num // 2
        answer += str(i+1) * cnt
    
    answer = answer + '0' + answer[::-1]
    return answer